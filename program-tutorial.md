# Programs

## 1) Hello world

Download `d3.min.js` from [d3js.org](https://d3js.org/) or else from [here](https://www.cdnpkg.com/d3/file/d3.min.js/)

Create a file `hello.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello World</title>
    <script src="d3.min.js"></script>
</head>
<body>
    <script>
        d3.select("body").append("p").text("Hello World!");
    </script>
</body>
</html>
```
in the above code Basically D3 will select the body element and append a paragraph element with the text "Hello World!".

or else you can use the following code:

```html
<!DOCTYPE html>
<html>
   <head>
      <script type = "text/javascript" src = "https://d3js.org/d3.v4.min.js"></script>
   </head>

   <body>
      <div class = "myclass">
         Hello World!
      </div>
      
      <script>
         d3.select("div.myclass").append("span").text("from D3.js");
      </script>
   </body>
</html>
```