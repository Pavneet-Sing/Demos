## For only android API (Android Pie)28 and +</h2>

To play gif(or jif :D) on API 28(Pie) and above you can use [AnimatedImageDrawable][1] although `Gilde` has been the first choice to play gif though [AnimatedImageDrawable][1] supports many features as shown:


   ```
   // kotlin
    // ImageView from layout
    val ima : ImageView = findViewById(R.id.img_gif)
    // create AnimatedDrawable
    val decodedAnimation = ImageDecoder.decodeDrawable(
            // create ImageDecoder.Source object
            ImageDecoder.createSource(resources, R.drawable.angry_kitty))
    // set the drawble as image source of ImageView
    ima.setImageDrawable(decodedAnimation)
    // play the animation
    (decodedAnimation as? AnimatedImageDrawable)?.start()
   ```

   ```
   // Java
   // ImageView from layout
   ImageView ima = findViewById(R.id.img_gif)
   // create AnimatedDrawable
   Drawable decodedAnimation = ImageDecoder.decodeDrawable(
               // create ImageDecoder.Source object
               ImageDecoder.createSource(getResources(), R.drawable.angry_kitty))
    // set the drawble as image source of ImageView
    ima.setImageDrawable(decodedAnimation)
    // play the animation
    (decodedAnimation as? AnimatedImageDrawable)?.start()
   ```


 XML code, add an ImageView

    ```
    <ImageView
        android:id="@+id/img_gif"
        android:background="@drawable/ic_launcher_background" <!--Default background-->
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_width="200dp"
        android:layout_height="200dp" />
    ```
`AnimatedImageDrawable` is a child of Drawable and created by `ImageDecoder.decodeDrawable`

`ImageDecoder.decodeDrawable` which further required the instance of `ImageDecoder.Source` created by `ImageDecoder.createSource`.

`ImageDecoder.createSource` can only take source as a name, ByteBuffer, File, resourceId, URI, ContentResolver to create source object and uses it to create `AnimatedImageDrawable` as `Drawable` (polymorphic call)

    static ImageDecoder.Source  createSource(AssetManager assets, String fileName)
    static ImageDecoder.Source  createSource(ByteBuffer buffer)
    static ImageDecoder.Source  createSource(File file)
    static ImageDecoder.Source  createSource(Resources res, int resId)
    static ImageDecoder.Source  createSource(ContentResolver cr, Uri uri)

Note: You can also create `Bitmap` using [ImageDecoder#decodeBitmap][2].

```
static Bitmap	decodeBitmap(ImageDecoder.Source src, ImageDecoder.OnHeaderDecodedListener listener)
static Bitmap	decodeBitmap(ImageDecoder.Source src)
```

Output:

![animation image demo](resources/animated_drawable.gif?raw=true "animated_drawable.gif")


### • Change Transparency

    // max 255 = opaque
    // min 0 = transparent
    decodedAnimation.alpha = 255/2


### • Color

- Change Color withLightingColorFilter


      // change color of gif, Multiplies the RGB channels by one color, and then adds a second color.
      val colorFilter = LightingColorFilter(Color.RED,Color.BLUE)
      decodedAnimation.colorFilter = colorFilter

- Change Color with PorterDuffColorFilter

      decodedAnimation.colorFilter = PorterDuffColorFilter(Color.RED,PorterDuff.Mode.DARKEN)

![animation image demo](resources/kitty_filter.gif?raw=true "kitty_filter.gif")

### • Change image shape

The [canvas][3] can be obtained to change the shape of the Animation object. In order to do this, A [PostProcessor][4] object is required to get the canvas object and should be linked with the animationdrawable via [ImageDecoder#setPostProcessor][5] method.

 - change the shape of canvas

         val decodedAnimation = ImageDecoder.decodeDrawable(
                 // create ImageDecoder.Source object
                 ImageDecoder.createSource(resources, R.drawable.tenor), { imageDecoder: ImageDecoder, imageInfo: ImageDecoder.ImageInfo, source: ImageDecoder.Source ->
                         imageDecoder.setPostProcessor( { canvas:Canvas ->
                                 val path = Path()
                                 path.fillType = Path.FillType.INVERSE_WINDING
                                 val width = canvas.width.toFloat()
                                 val height = canvas.height.toFloat()
                                 path.addRoundRect(0f, 0f, width, height, 100f, 100f, Path.Direction.CW)
                                 val paint = Paint()
                                 paint.isAntiAlias = true
                                 paint.color = Color.TRANSPARENT
                                 paint.xfermode = PorterDuffXfermode(PorterDuff.Mode.SRC)
                                 canvas.drawPath(path, paint)
                             return@setPostProcessor PixelFormat.TRANSLUCENT

                         })
                 }
         )


![animation image demo](resources/kitty_in_circle.png?raw=true "kitty_in_circle.png")


  [1]: https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable
  [2]: https://developer.android.com/reference/android/graphics/ImageDecoder.html#decodeBitmap(android.graphics.ImageDecoder.Source)
  [3]: https://developer.android.com/reference/android/graphics/Canvas
  [4]: https://developer.android.com/reference/android/graphics/PostProcessor
  [5]: https://developer.android.com/reference/android/graphics/ImageDecoder.html#setPostProcessor(android.graphics.PostProcessor)
