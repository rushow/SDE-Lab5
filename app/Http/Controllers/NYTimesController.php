<?php

namespace App;
namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests\ProfileRequest;
use App\Http\Requests\PasswordRequest;
use Illuminate\Support\Facades\Hash;

use App\SocialPost;
use Illuminate\Support\Facades\Http;

class NYTimesController extends Controller
{
    /**
     * Show the form for editing the profile.
     *
     * @return \Illuminate\View\View
     */
    public function index(Request $request)
    {
        $response_json = Http::get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key=W1hafgsykUqecrPRjQpk4vAzXsfWMHqH');

        $response = json_decode($response_json);
        $results = $response->results;
   

        foreach($results as $result){
            $social_post = new SocialPost();
            $social_post->api_name = 'nytimes';
            $social_post->title = $result->title;
            $social_post->abstract = $result->abstract;
            $social_post->item_type = $result->item_type;
            $social_post->url = $result->url;
            $social_post->uri = $result->uri;
            $social_post->published_date = date('Y-m-d', strtotime($result->published_date));
            $social_post->save();
        }

        // return view('nytimes', ['results' => $results]);
        return response()->json([
            'message' => 'Successfully imported data from NY Times!'
        ], 201);
    }
}
