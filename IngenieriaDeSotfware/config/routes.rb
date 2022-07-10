Rails.application.routes.draw do

  mount RailsAdmin::Engine => 'admin', as: 'rails_admin'
  get 'matches/index'
  get 'matches/show'
  get 'matches/new'
  get 'matches/create'
  resources :cita
  resources :gustos
  root 'welcome#home', as: :home
  devise_for :users, controllers: { sessions: 'users/sessions', registrations: 'users/registrations'}
  get 'user/user_gustos', to: 'users#show_user_gustos', as: :show_user_gustos
  get 'user/recommendations', to: 'users#show_user_recommendations', as: :show_user_recommendations
  get 'user/:user_id/add_gusto/:gusto_id', to: 'gustos#add_user_gusto', as: :add_user_gusto
  get 'user/:user_id/delete_gusto/:gusto_id', to: 'gustos#delete_user_gusto', as: :delete_user_gusto
  get 'user/user_matches', to: 'users#show_user_matches', as: :show_user_matches
  get 'user/user_postulations', to: 'users#show_user_postulations', as: :show_user_postulations
  get 'user/user_dates', to: 'users#show_user_dates', as: :show_user_dates
  get 'user/user_restaurants', to: 'users#show_user_restaurants', as: :show_user_restaurants
  get 'user/admin/edit/:id', to: 'users#edit_user_by_admin', as: :edit_user_by_admin
  get 'user/recommendations/new_match', to: 'matches#create', as: :new_user_match
  patch 'user/admin/edit/:id', to: 'users#update_user_by_admin'
  get 'user/admin/show/:id', to: 'users#show_user_to_admin', as: :show_user_to_admin
  get 'user/admin/postulations', to: 'restaurants#show_postulations', as: :restaurants_postulations
  patch 'user/admin/postulations', to: 'restaurants#update_postulation', as: :update_postulation
  patch 'user/user_dates', to: 'cita#check_citum', as: :check_citum

  # READ Users
  get 'users', to: 'users#index', as: :index_users
  get 'user/profile', to: 'users#show', as: :show_user

  # CREATE Comments
  get 'comments/new', to: 'comments#new'
  post 'comments', to: 'comments#create'

  # READ Comments
  get 'comments', to: 'comments#index', as: :index_comments
  get 'comments/:id', to: 'comments#show', as: :comment

  # UPDATE Comments
  get 'comments/:id/edit', to: 'comments#edit', as: :comment_edit
  patch 'comments/:id', to: 'comments#update'
  put 'comments/:id', to: 'comments#update'

  # DELETE Comments
  delete 'comments/:id', to: 'comments#destroy'

  # CREATE Cities
  get 'cities/new', to: 'cities#new'
  post 'cities', to: 'cities#create'

  # READ Cities
  get 'cities', to: 'cities#index'
  get 'cities/:id', to: 'cities#show', as: :city

  # UPDATE Cities
  get 'cities/:id/edit', to: 'cities#edit', as: :city_edit
  patch 'cities/:id', to: 'cities#update'

  # DELETE Cities
  delete 'cities/:id', to: 'cities#destroy'

  # SCAFFOLD Restaurants
  resources :restaurants
end
