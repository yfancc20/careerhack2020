<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    protected $COLORS = [
        '(255, 255, 0, 0.3)', '(255, 165, 0, 0.3)', '(255, 255, 0, 0.3)', '(154, 205, 50, 0.2)', '(0, 191, 255, 0.2)'
    ];

    public function pageList(Request $request) {
        return view('page_list');
    }

    public function showPage(Request $request, $num) {
        $path = storage_path() . '/json/lines_' . sprintf('%04d', $num) .  '.json';
        $data = json_decode(file_get_contents($path), true);

        $labelData = $this->labelColor($data);

        ksort($labelData);

        $imageFile = 'labeling_' . sprintf('%04d', $num) . '.jpg';
        return view('page', compact('imageFile', 'num', 'labelData'));
    }

    public function showTestPage(Request $request, $num) {
        $path = storage_path() . '/json/test/lines_' . sprintf('%04d', $num) .  '.json';
        $data = json_decode(file_get_contents($path), true);

        $labelData = $this->labelColor($data);

        ksort($labelData);

        $imageFile = 'labeling_' . sprintf('%04d', $num) . '.jpg';
        return view('page_test', compact('imageFile', 'num', 'labelData'));
    }

    private function labelColor($data) {
        $labelData = [];
        $i = 0;
        foreach ($data as $d) {
            $d['id'] = $i;
            $i += 1;
            if (array_key_exists('label', $d)) {
                if ($d['label'] <= 2) {
                    $d['color'] = $this->COLORS[$d['label']];
                    $labelData[0][] = $d;
                } else if ($d['label'] === 99) {
                    $d['color'] = $this->COLORS[4];
                    $labelData[99][] = $d;
                } else if ($d['label'] % 2 === 1) {
                    // odd 
                    $d['color'] = $this->COLORS[3];
                    $labelData[3][] = $d;
                } else {
                    // even
                    $d['color'] = $this->COLORS[4];
                    $labelData[4][] = $d;
                }
            } else {
                $labelData[99][] = $d;
            }
        }
        return $labelData;
    }

    public function process(Request $request) {
        $text = $request->input('text');
        $num = $request->input('num');
        $type = $request->input('type');

        $path = '';
        if ($type === 'test') {
            $path = storage_path() . '/input/test/labeling_' . sprintf('%04d', $num) .  '.json';
        } else {
            $path = storage_path() . '/input/labeling_' . sprintf('%04d', $num) .  '.json';
        }

        $data = json_decode(file_get_contents($path), true);

        $lines = $data['recognitionResults'][0]['lines'];

        $flag = false;
        foreach ($lines as $line) {
            foreach ($line['words'] as $word) {
                if ($word['text'] === $text) {
                    $output = [
                        'text' => $text,
                        'elements' => $word['boundingBox'],
                    ];
                    $flag = true;
                    break;
                }
            }
            if ($flag) {
                break;
            }
        }

        if ($type === 'test') {
            $path = storage_path() . '/outputtest/labeling_' . sprintf('%04d', $num) .  '.json';
        } else {
            $path = storage_path() . '/output/labeling_' . sprintf('%04d', $num) .  '.json';
        }

        $newJsonString = json_encode($output, JSON_PRETTY_PRINT);
        $result = file_put_contents($path, stripslashes($newJsonString));

        return $result;
    }
}
