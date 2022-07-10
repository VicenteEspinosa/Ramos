Rails.application.routes.draw do
  resources :shopping_carts
  put 'pay_cart/:id', to: 'shopping_carts#pay_cart'
  resources :coupons
  resources :cart_items
  resources :products
  resources :categories
  resources :used_coupons

  get 'shopping_history/:id', to: 'shopping_carts#shopping_history'
  post 'coupons/verify', to: 'coupons#verify'

  devise_for :users,
  controllers: {
      sessions: 'users/sessions',
      registrations: 'users/registrations'
  }
end
