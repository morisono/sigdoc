# Python Lambdaについて

1. lambda : binarize_image(images, tmpd）

1. lambda images, tmpd: binarize_image(images, tmpd)

1. lambda images=input_images, tmpd=tmpd: binarize_image(images, tmpd)

どっちが正しい？違いは？

---
両方の lambda 関数の形式は正しいですが、使い方に微妙な違いがあります。

1は、引数を受け取らない lambda 関数です。binarize_image 関数に images と tmpd を引数として渡すことはできません。代わりに、binarize_image 関数内でこれらの変数を参照する必要があります。

2は、images と tmpd を引数として受け取り、binarize_image 関数を呼び出す lambda 関数です。この形式では、実際に関数を呼び出す際に引数を指定する必要があります。

3は、images と tmpd のデフォルト引数値を設定した lambda 関数です。この形式を使用することで、images と tmpd が関数呼び出し時に渡されなかった場合に、デフォルト引数として input_images と tmpd の値が使用されるようになります。

どちらの形式を選ぶかは、使用するコンテキストによります。もし images と tmpd が外部から渡される変数である場合は、1番目の形式を使用して関数呼び出し時に引数を渡す方が適切です。一方で、これらの変数が関数内で定義されている場合は、2番目の形式を使用して関数内で直接参照する方が適切です。
