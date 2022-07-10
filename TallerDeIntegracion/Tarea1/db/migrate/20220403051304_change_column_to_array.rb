class ChangeColumnToArray < ActiveRecord::Migration[7.0]
  def change
    change_column :users, :operations, :string, array: true, default: []
  end
end
