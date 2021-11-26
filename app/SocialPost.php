<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class SocialPost extends Model
{
    protected $fillable = [
        'api_name', 'title', 'abstract', 'item_type', 'url', 'uri', 'published_date'
    ];

    public function socialtags()
    {
    	return $this->hasMany(SocialTag::class);
    }
}
