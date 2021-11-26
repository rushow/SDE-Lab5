<?php

namespace App\Http\Controllers;

use App\Http\Resources\SocialTagResource;
use App\SocialPost;
use App\Review;
use Illuminate\Http\Request;

class SocialTagController extends Controller
{
    public function index(SocialPost $social_post)
    {
       return SocialTagResource::collection($social_post->social_tag);
         
    }

    public function store(SocialTagRequest $request , SocialPost $social_post)
    {
        $social_tag = new SocialTag($request->all());
       
        $social_post->socialtags()->save($social_tag);
      
       return response([
         'data' => new SocialTagResource($social_tag)
       ],Response::HTTP_CREATED);
    }

    public function update(Request $request, SocialPost $social_post, SocialTag $social_tag)
    {
        $social_tag->update($request->all());
    }

    public function destroy(SocialPost $social_post, SocialTag $social_tag)
    {
        $social_tag->delete();
        return response(null,Response::HTTP_NO_CONTENT);
    }
}
