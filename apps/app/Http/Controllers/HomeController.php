<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function pageList(Request $request) {
        return view('page_list');
    }

    public function showPage(Request $request, $num) {
        $path = storage_path() . '/json/lines_' . sprintf('%04d', $num) .  '.json';
        $json = json_decode(file_get_contents($path), true); 

        $imageFile = 'labeling_origin_' . sprintf('%04d', $num) . '.jpg';
        return view('page', compact('imageFile', 'num'));
    }
}
