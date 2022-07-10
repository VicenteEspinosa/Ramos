class ChangeOperationsToText < ActiveRecord::Migration[7.0]
  def change
    change_column :users, :operations, :text, array: true, default: []
  end
end
