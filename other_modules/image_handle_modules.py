# default
import imgbbpy, wget, os, asyncio, time
from dataclasses import dataclass
from typing import Optional

# local
from all_env import IMGBB_API_KEY
sync_client = imgbbpy.SyncClient(IMGBB_API_KEY)
async_client = imgbbpy.AsyncClient(IMGBB_API_KEY)

def save_image(url):
	image = wget.download(url)
	return image

def delete_image(image):
	# time.sleep(2)
	os.remove(image)

@dataclass
class SyncImgbb:
	url: Optional[str] = None
	path: Optional[str] = None

	def upload(self):
		if self.url:
			image = save_image(self.url)
			link = self.upload_imgbb_image(image)
			delete_image(image)
			return link
		elif self.path:
			link = self.upload_imgbb_image(image)
			return link
		return None

	def upload_imgbb_image(image):
		img = sync_client.upload(file=image)
		return img.url


@dataclass
class SyncImgbb:
	url: Optional[str] = None
	path: Optional[str] = None

	async def upload(self):
		if self.url:
			image = save_image(self.url)
			link = await self.upload_imgbb_image(image)
			delete_image(image)
			return link
		elif self.path:
			link = await self.upload_imgbb_image(image)
			return link
		return None

	async def upload_imgbb_image(image):
		img = await async_client.upload(file=image)
		return img.url


# def imgbb_image(url:str):
# 	image = save_image(url)
# 	link = upload_imgbb_image(image)
# 	print(link)
# 	delete_image(image)

# 	return link

# def crop_image(url):
# 	image = save_image(url)
# 	print(image)
# 	img = cv2.imread(image)
# 	print(img.shape) # Print image shape

# 	# resize image
# 	resized_img = cv2.resize(img,(382, 200), interpolation = cv2.INTER_AREA)
# 	# Cropping an image
# 	cropped_image = resized_img[0:200,91:291]

# 	# Save the cropped image
# 	cv2.imwrite("cropped-"+str(image), cropped_image)

# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()

# 	delete_image(image)

# 	return "cropped-"+str(image)