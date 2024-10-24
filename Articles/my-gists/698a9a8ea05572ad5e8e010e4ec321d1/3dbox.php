<?php

    ini_set('display_errors',1);
      $handle =  new Imagick('Wallpaper1.jpg');
       $depth = '1';

        $edge = $depth * 72;

        $width  = $handle->getImageWidth() ;// - ( $edge * 2 );
        $height = $handle->getImageHeight() ;//- ( $edge * 2 );

        $shrink    = round(( $edge * 0.7 ), 2);
        $angle     = 30; 
        $radian    = ( $angle * Pi() ) / 180;
        $alpha     = round((abs(tan($radian)) * $shrink), 2);
        $shortSide = round( ($height - $alpha ), 2);

        $topLong   = round($width + $shrink, 2);
        $handle->setImageFormat('png');

        /**
         * Central part
         */
        $centralPart = clone $handle;
        // for morror $centralPart->cropImage($width, $height, 0, 0);
        // for normal
        $centralPart->cropImage($width -$edge, $height-$edge, 0, 0);
//        $centralPart->borderImage(new ImagickPixel("transparent"), 1, 1);
        
        /**
         * Right corner
         */
        $rightCorner = clone $handle;
        $rightCorner->cropImage($edge, $height, $width - $edge, 0);
        $rightCorner->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);
        $rightCorner->setBackgroundColor(new ImagickPixel('transparent')); 
        $rightCorner->setImageMatte(true);  
        
       $rightCorner->distortImage(Imagick::DISTORTION_PERSPECTIVE, array(
            
            0, 0, 0, 0,# top left 

            $edge, 0, $shrink,$alpha,# top right

            $edge, $height, $shrink, $height+$alpha,# bottom right

            0, $height, 0, $height# bottum left
        ), true); 
         
         /**
         * Top part
         */
        $topCorner = clone $handle;
        $topCorner->cropImage($handle->getImageWidth()-$edge, $edge, 0, $handle->getImageHeight()-$edge);
        $topCorner->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);
        $topCorner->setImageMatte(true);
        $topCorner->setBackgroundColor(new ImagickPixel('transparent'));
        //$topCorner->rotateImage(new ImagickPixel("transparent"), 180);
        //$topCorner->flopImage();
        //$topCorner->borderImage(new ImagickPixel("transparent"), 0, 0); 
     //   $topCorner->trimImage('0');
        $topCorner->distortImage(Imagick::DISTORTION_PERSPECTIVE, array(
            0, 0, 0, 0,

            $width, 0,$width, 0,

            $width, $edge,$topLong, $alpha,

            0, $edge,$shrink, $alpha
        ), true);
         
      
        /**
         * Composite image
         */
         
        $handle = new Imagick();
        $handle->newImage(
            $rightCorner->getImageWidth() + $centralPart->getImageWidth(),
            $topCorner->getImageHeight() + $centralPart->getImageHeight(),
            new ImagickPixel('transparent')
        );
        $handle->setBackgroundColor(new ImagickPixel('transparent'));
        $handle->setImageFormat('png');
        $handle->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT); 
     
        $handle->compositeimage($centralPart, Imagick::COMPOSITE_DEFAULT, 0, 0);
        $handle->compositeimage($rightCorner, Imagick::COMPOSITE_DEFAULT, $centralPart->getImageWidth(), 0);
        $handle->compositeimage($topCorner, Imagick::COMPOSITE_DEFAULT, 0, $centralPart->getImageHeight()-1);
                 /*create shadow of image */
        $shadow = $handle->clone(); 
        $shadow->setImageBackgroundColor( new ImagickPixel( 'black' ) ); 
        $shadow->shadowImage( 80, 3, 5, 5 ); 
        $shadow->compositeImage( $handle, Imagick::COMPOSITE_OVER, 0, 0 );
       
        /*create shadow of image */
        
        $shadow->writeImage('wrap1.png');
        
        header('Content-Type: image/png'); 
        echo $shadow;
        die();
        

?>