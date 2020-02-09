<!doctype html>
<html lang="{{ app()->getLocale() }}">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="{{ asset('/css/bootstrap.min.css') }}" rel="stylesheet">
        <link href="{{ asset('/css/fontawesome-all.css') }}" rel="stylesheet">
        <link href="{{ asset('/css/style.css') }}" rel="stylesheet">

        <script src="{{ asset('/js/jquery.min.js') }}"></script>

        <title>Testing...</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="container">
            <h2 class="text-center title">
                <span>
                    <a href="{{ url('page/test/' . ($num - 1)) }}">
                        <i class="far fa-angle-left arrow"></i>
                    </a>
                </span>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                {{ $num }}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <span>
                    <a href="{{ url('page/test/' . ($num + 1)) }}">
                        <i class="far fa-angle-right arrow"></i>
                    </a>
                </span>
            </h2>
            
            <div class="row">
                <div class="col-6 image-box pt-2">
                    <img src="{{ asset('/input/test/' . $imageFile) }}" class="input-image">
                </div>
                <div class="col-6">
                    <div class="row">
                    @foreach ($labelData as $key => $data)
                        @if ($key <= 2)
                            <div class="label-box-top p-2 col-12">
                                @foreach ($data as $d)
                                    <a class="lines" href="" data-id="{{$d['id']}}">
                                    <button class="btn btn-light my-1 textTag" data-id="{{$d['id']}}"
                                    style="background-color:rgba{{$d['color']}}">{{ $d['text'] }}</button>
                                    </a>
                                @endforeach
                            </div>
                        @elseif ($key <= 4 && $key >=3)
                            <div class="label-box-mid mb-1 p-2 col-6">
                                @foreach ($data as $d)
                                    <a class="lines textTag" href="" data-id="{{$d['id']}}">
                                        <p><button class="btn btn-light my-1" data-id="{{$d['id']}}"
                                            style="background-color:rgba{{$d['color']}}">{{ $d['text'] }}</button>
                                        </p>
                                    </a>
                                @endforeach
                            </div>
                        @else
                            <div class="label-box-bottom mb-1 p-2">
                                @foreach ($data as $d)
                                    <a class="lines" href="" data-id="{{$d['id']}}">
                                        <button class="btn btn-light my-1 textTag" data-id="{{$d['id']}}">{{ $d['text'] }}</button>
                                    </a>
                                @endforeach
                            </div>
                        @endif
                    @endforeach
                    </div>
                </div>
            </div>
            <div class="text-center">
                
                
            </div>
        </div>
    </body>
    <script>
        $(function () {
            $('.textTag').click(function(e) {
                e.preventDefault();
                $.ajax({
                    url: '{{ url('page/process') }}',
                    method: 'POST',
                    data: {
                        _token: '{{ csrf_token() }}',
                        id: $(this).data('id'),
                        num: {{ $num }},
                        type: 'test',
                    },
                    dataType: 'json'
                }).done(function(result) {
                    location.href = '{{ url('page/test/' . ($num + 1)) }}';
                });
            });
        })
    </script>
</html>
