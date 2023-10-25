from django import forms

class TrackingForm(forms.Form):
    html_content_1 = forms.CharField(
        label='粘贴HTML内容',
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"}
        ),
        required=False
    )
    html_content_2 = forms.CharField(
        label='粘贴HTML内容',
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"}
        ),
        required=False
    )
    html_content_3 = forms.CharField(
        label='粘贴HTML内容',
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"}
        ),
        required=False
    )
