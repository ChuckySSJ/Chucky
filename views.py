from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.
def index(request):
	contenido = """
		<html>
			<head>
				<title>lopez renteria jose manuel</title>
			<head>
			<body>
				<h1>lopez renteria jose manuel</h1>
			</body>
			<style>	
				body{
					background-color: red;
					color: white;
					font-size: 30px; 
					text-align:center;
				}

			</style>
		</html>		
	"""
	return HttpResponse(contenido)