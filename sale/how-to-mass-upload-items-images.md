# How to mass upload items images?

You can add images to all sale items without the need to manually upload them one by one.

1. Prepare the images files: in order to connect the images to the items, you need to give the file a pattern name that contains the item ID \(ID is shown next to the item title\).

   Example: for item ID 777 name the image file `777.png`.

   If you have multiple images for one item use the underscore \( \_ \) character to identify it.

   Example: item ID 777 will get the following images attached to it: `777.png`, `777_1.png`, `777_abc.jpg` etc.

![](https://user-images.githubusercontent.com/20393485/47136635-f459a380-d2bc-11e8-85b6-7d68c5d116cc.jpg)

1. Open your Amazon S3 bucket, create a directory and name it with the sale ID \(ID is shown next to the sale title\). 

![](https://user-images.githubusercontent.com/20393485/47136695-32ef5e00-d2bd-11e8-82b4-4a9c2bc69b2f.jpg)

1. Upload all the sale images to the Amazon directory.
2. Click on **Sync item images** to sync the images from Amazon to your system.

![](https://user-images.githubusercontent.com/20393485/47136762-63cf9300-d2bd-11e8-9dc2-4bd1ffbd4d88.jpg)

