class AddSucursalToReservas < ActiveRecord::Migration[7.0]
  def change
    add_column :reservas, :sucursal, :string
  end
end
