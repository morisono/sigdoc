const xlinkNS = 'http://www.w3.org/1999/xlink'

const triggerDownload = (fileName, imgURI) => {
  const evt = new MouseEvent('click', {
    view: window,
    bubbles: false,
    cancelable: true
  });

  const a = document.createElement('a');
  a.setAttribute('download', `${fileName}.png`);
  a.setAttribute('href', imgURI);
  a.setAttribute('target', '_blank');

  a.dispatchEvent(evt);
}

const exportDoc = (fileName, svg) => {
  const svgData = (new XMLSerializer()).serializeToString(svg)
  const svgURL = `data:image/svg+xml;base64,${btoa(svgData)}`

  const svgImg = document.createElement('img')

  svgImg.onload = function() {
    const canvas = document.createElement('canvas')
    canvas.width = svgImg.width
    canvas.height = svgImg.height

    canvas.getContext('2d').drawImage(svgImg, 0, 0)

    triggerDownload(fileName, canvas.toDataURL('image/png'))
  }

  svgImg.src = svgURL
}

const imgToDataUrl = inputImage => {
  return new Promise((resolve, reject) => {
    const img = document.createElement('img')

    img.onload = () => {
      const canvas = document.createElement('canvas')
      canvas.width = img.width
      canvas.height = img.height
      canvas.getContext('2d').drawImage(img, 0, 0)

      inputImage.setAttributeNS(xlinkNS, 'href', canvas.toDataURL())

      resolve(inputImage)
    }
  	
    img.onerror = () => {
      const oldSrc = img.src
      img.onerror = () => {
        console.warn(`failed to load an image at: ${img.src}`)
        resolve(inputImage)
      }
      img.src = ''
      img.src = oldSrc
    }

    img.src = inputImage.getAttributeNS(xlinkNS, 'href')
  })
}

const downloadSvg = (fileName, svg) => {
  const hasHrefAttribute = image => image.getAttributeNS(xlinkNS, 'href').indexOf('data:image') < 0
  const processedImages = Array.from(svg.querySelectorAll('image'))
    .filter(hasHrefAttribute)
    .map(imgToDataUrl)

  Promise.all(processedImages)
    .then(() => exportDoc(fileName, svg))
}

document.getElementById('download-button').onclick = () => {
	const svg = document.getElementById('generated-svg')
  const fileName = 'test-file'
  
  downloadSvg(fileName, svg)
}