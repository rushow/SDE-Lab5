<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class SocialPost extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true; //Only authorize user can do this operation if false then unauthorize user can do
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
            'title' => 'required',
            'abstract' => 'required',
            'item_type' => 'required',
            'url' => 'required',
            'uri' => 'required'
        ];
    }
}
