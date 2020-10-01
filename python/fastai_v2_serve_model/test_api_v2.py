# import library
from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn
import urllib.request
import io

#
from fastai.vision.all import *

app = Starlette(debug=True)

# test api
@app.route("/classify-url", methods=["GET"])
async def classify_url(request):

	print("1", request.query_params["url"])

	url = request.query_params["url"]
	response = urllib.request.urlopen(url)
	bytes  = response.read()      # a `bytes` object

	# there is no get_bytes function...
	# bytes = await get_bytes(request.query_params["url"])
	img = PILImage.create(io.BytesIO(bytes))
	# img = open_image(BytesIO(bytes))
	predicted_class , predicted_index, losses = learn_inf.predict(img)
	print("predicted:", predicted_class, predicted_index.item(), losses.numpy())

	# return JSONResponse({
	# 	'status': 'ok'
	# })

	return JSONResponse({
		'url': url,
		'predicted_class': predicted_class,
		'predicted_index': predicted_index.item(),
		'score': losses.numpy().tolist(),
	})

	# return JSONResponse({
	# 	"predictions": sorted(
	# 		zip(learn_inf.data.classes, map(float, losses)),
	# 		key=lambda p: p[1],
	# 		reverse=True
	# 	)
	# })


def prepare_model(path):
	global learn_inf
	learn_inf = load_learner(path+'export.pkl')
	# learn_inf = load_learner(path)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print("starting server...")

	prepare_model(path='./models/')

	uvicorn.run(app, host='0.0.0.0', port=8000)
