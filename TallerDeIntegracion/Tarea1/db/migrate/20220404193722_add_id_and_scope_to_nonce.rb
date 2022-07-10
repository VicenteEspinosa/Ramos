class AddIdAndScopeToNonce < ActiveRecord::Migration[7.0]
  def change
    add_column :nonces, :user_id, :string
    add_column :nonces, :scopes, :text, array:true
  end
end
