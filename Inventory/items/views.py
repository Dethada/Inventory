# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Items

# Create your views here.
@login_required(login_url='/login')
def index(request):
	items = Items.objects.all()

	context = {'items': items}
	return render(request, 'index.html', context)

@login_required(login_url='/login')
def add(request):
	if(request.method == 'POST'):
		title = request.POST['title'].strip()
		quantity = request.POST['quantity']
		unit = request.POST['unit']
		category = request.POST['category']
		created = request.POST['created_at']
		expires = request.POST['expires_at']
		
		if Items.objects.filter(title=title).exists():
			messages.error(request, "Error: Item name already exist")
		else:
			if (expires == '' or expires == 'None'):
				item = Items(title=title, quantity=quantity, unit=unit, category=category, created_at=created)
			else:
				item = Items(title=title, quantity=quantity, unit=unit, category=category, created_at=created, expires_at=expires)
			item.save()

		return redirect('/')
	else:
		return render(request, 'add.html')

@login_required(login_url='/login')
def edit(request, pk):
	if(request.method == 'POST'):
		quantity = request.POST['quantity']
		category = request.POST['category']
		expires = request.POST['expires_at']

		if (expires == '' or expires == 'None'):
			Items.objects.filter(pk=pk).update(quantity=quantity)
			Items.objects.filter(pk=pk).update(category=category)
		else:
			Items.objects.filter(pk=pk).update(quantity=quantity)
			Items.objects.filter(pk=pk).update(category=category)
			Items.objects.filter(pk=pk).update(expires_at=expires)
		#item.save()

		return redirect('/')
	else:
		item = Items.objects.get(id=pk)

		context = {'item': item}
		return render(request, 'edit.html', context)

@login_required(login_url='/login')
def increment(request, pk):
	i = 1 + Items.objects.values_list('quantity', flat=True).get(pk=pk)
	Items.objects.filter(pk=pk).update(quantity=i)
	return redirect('/')

@login_required(login_url='/login')
def decrement(request, pk):
	i = Items.objects.values_list('quantity', flat=True).get(pk=pk) - 1
	if (i > 0):
		Items.objects.filter(pk=pk).update(quantity=i)
	return redirect('/')

@login_required(login_url='/login')
def delete(request, pk):
	Items.objects.filter(id=pk).delete()
	return redirect('/')
