<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class SocialTag extends Model
{
    protected $fillable = [
        'sp_id', 'tags'
    ];

    public function socialpost()
    {
    	return $this->belongsTo(SocialPost::class);
    }
}
