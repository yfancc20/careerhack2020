<!doctype html>
<html lang="{{ app()->getLocale() }}">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="{{ asset('/css/bootstrap.min.css') }}" rel="stylesheet">
        <link href="{{ asset('/css/style.css') }}" rel="stylesheet">

        <title>Processing...</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="container mt-5">
        <h2 class="text-center my-5">{{ 'Input ' . $num }}</h2>
        <div class="row">
            <div class="col-6">
                <img src="{{ asset('/input/' . $imageFile) }}" class="input-image">
            </div>
        </div>
        
            
        </div>
    </body>
</html>
