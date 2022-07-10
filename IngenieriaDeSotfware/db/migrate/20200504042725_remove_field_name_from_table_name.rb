class RemoveFieldNameFromTableName < ActiveRecord::Migration[5.2]
  def change
    remove_column :cities, :city_id, :datatype
  end
end
