Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      get 'reset', to: 'users#reset'
      get 'users/:id', to: 'users#get'
      post 'users', to: 'users#create'
      patch 'users/:id', to: 'users#patch'
      delete 'users/:id', to: 'users#delete'

      get 'users/:id/:scope', to: 'users#get_scoped'

      get 'oauth/request', to: 'oauth#request_token'
      get 'oauth/grant', to: 'users#grant'
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
