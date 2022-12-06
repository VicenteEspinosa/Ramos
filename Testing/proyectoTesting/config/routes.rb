# frozen_string_literal: true

Rails.application.routes.draw do
  # resources :products
  get 'reservas/new/:sala/:fecha/:horario', to: 'reservas#new', as: 'new_reserva'
  post 'reservas/new/:sala/:fecha/:horario', to: 'reservas#create'
  delete 'products/:id', to: 'products#destroy'
  post 'products/:id/edit', to: 'products#edit'
  patch 'products/:id', to: 'products#update'
  get 'products/new', to: 'products#new'
  post 'products', to: 'products#create'
  get 'products/:id', to: 'products#show'
  get 'products', to: 'products#index'
  get 'products/:category/category', to: 'products#filter_by_category'
  get 'movie/new'
  post 'movie/new', to: 'movie#post', as: 'create_movie'
  post 'movie_time/new', to: 'movie#create_movie_time', as: 'new_movie_time'
  get '/', to: 'movie#home', as: 'home'
  get 'movies/list', to: 'movie#list_by_date', as: 'movies_by_date'
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  get 'products/list', to: 'product#index'
  get 'filter_by_category/:category', to: 'products#filter_by_category'
end
