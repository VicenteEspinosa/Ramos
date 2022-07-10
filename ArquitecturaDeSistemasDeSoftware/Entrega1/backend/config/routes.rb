Rails.application.routes.draw do
  resources :locations
    namespace :api do
      namespace :v1 do
        get 'users', to: 'users#index'
        post 'user/login', to: 'users#login'

        get 'user/:id', to: 'users#show'
        post 'user/create', to: 'users#create'

        post 'location/create', to: 'locations#create'
        get 'locations', to: 'locations#index'

        get 'locations/:user_id', to: 'locations#user_locations'
        get 'locations/users/:users_ids', to: 'locations#multiple_user_locations'

        get 'pings/:user_id', to: 'ping#user_ping'
        post 'ping/create', to: 'ping#create'
      end
    end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
