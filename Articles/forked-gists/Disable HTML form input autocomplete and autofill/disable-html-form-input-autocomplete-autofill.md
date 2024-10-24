# Disable HTML Form Input Autocomplete and Autofill

1. Add `autocomplete="off"` onto `<form>` element;
2. Add hidden `<input>` with `autocomplete="false"` as a first children element of the form.

````html
<form autocomplete="off" method="post" action="">
    <input autocomplete="false" name="hidden" type="text" style="display:none;">
    ...
````

This formation is going to prevent Chrome and Firefox to offer autofill and autocomplete for all input fields inside the form.