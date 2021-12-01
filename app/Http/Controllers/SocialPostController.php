<?php

namespace App\Http\Controllers;
use App\Http\Requests\SocialPostRequest;
use App\Http\Resources\SocialPostCollection;
use App\Http\Resources\SocialPostResource;
use App\SocialPost;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class SocialPostController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth:api')->except('index','show');
    }

   
    public function index(Request $request)
    {
        $social_post = SocialPost::all();
        return response()->json($social_post);
    }
    
    public function store(SocialPostRequest $request)
    {
       $social_post = new SocialPost;
       $social_post->title = $request->title;
       $social_post->abstract = $request->abstract;
       $social_post->item_type = $request->item_type;
       $social_post->url = $request->url;
       $social_post->uri = $request->uri;
       $social_post->published_date = $request->published_date;

       $social_post->save();

       return response([

         'data' => new SocialPostResource($social_post)

       ],Response::HTTP_CREATED);

    }

    public function show(SocialPost $social_post)
    {
        return new SocialPostResource($social_post);
    }
    
    public function update(Request $request, SocialPost $social_post)
    {   
        $this->userAuthorize($social_post);

        $request['detail'] = $request->description;

        unset($request['description']);

        $social_post->update($request->all());

       return response([

         'data' => new SocialPostResource($social_post)

       ],Response::HTTP_CREATED);

    }
   
    public function destroy(SocialPost $social_post)
    {
        $social_post->delete();

        return response(null,Response::HTTP_NO_CONTENT);
    }

     public function userAuthorize($social_post)
    {
        if(Auth::user()->id != $social_post->user_id){
            //throw your exception text here;
            
        }
    }
}
