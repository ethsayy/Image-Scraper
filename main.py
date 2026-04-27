import requests,tkinter,time
from pathlib import Path
from bs4 import BeautifulSoup

root = tkinter.Tk()
root.title('Image Scraper')
root.geometry('600x300')
root.resizable(False, False)

images_path = Path.cwd() / 'images'

def image_scrape():
    url = str(url_button.get())
    url_name = url
    url_name = url_name.replace('.','').replace('/', '').replace('-', '_').replace(':', '').removeprefix('httpswww')
    Path.mkdir(images_path / url_name)
    url_path = images_path / url_name
    try:
        request = requests.get(url)
        print(request.status_code)
        soup = BeautifulSoup(request.text, 'html.parser')
        iterations = 0
        for image in soup.find_all('img'):
            time.sleep(0.5)
            image_source = image.get('src')
            image_name = str(iterations) + '.png'
            with open(url_path / image_name, 'wb') as f:
                if not (image_source.startswith('https')):
                    image_source = 'https://' + image_source
                f.write(requests.get(image_source).content)
            iterations += 1
        print('Done')
    except Exception as e:
        print(e)

tkinter.Label(root, text='Enter URL: ').grid(row=0, column=0)
url_button = tkinter.Entry(root, width=80)
url_button.grid(row=0,column=1)


scrape_button = tkinter.Button(root, text='SCRAPE!',command=image_scrape,width=50).grid(row=1, column=1)
root.mainloop()