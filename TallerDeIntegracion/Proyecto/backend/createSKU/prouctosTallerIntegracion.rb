require 'rubygems'
require 'base64'
require 'hmac-sha1'
require 'net/http'
require 'uri'
require 'json'

@productos_file = JSON.parse(File.read('./productos.json'))

@key = "4PAKDkeMljd@VPI"
@base_url = "https://prod.api-bodega.2022-1.tallerdeintegracion.cl/bodega/"
@almacenes_no_cocina = ["627ed4faee1e5e6e0f313fd2", "627ed4faee1e5ee1e4313fd1", "627ed4faee1e5e2cc4313fd0", "627ed4faee1e5e2521313fcf"]
@cocina = "627ed4faee1e5e2785313fd3"

def puts_red(string)
    puts "\e[31m#{string}\e[0m"
end

def puts_blue(string)
    puts "\e[34m#{string}\e[0m"
end

def puts_black(string)
    puts "\e[30m#{string}\e[0m"
end

def puts_purple(string)
    puts "\e[35m#{string}\e[0m"
end

def puts_green(string)
    puts "\e[32m#{string}\e[0m"
end

def product_requirements(sku)
    @productos_file[sku]["requires"]
end

def product_batch(sku)
    @productos_file[sku]["batch_size"]
end

def get_auth(to_encode="GET")
    hmac_sha1.update(to_encode)
    "INTEGRACION grupo13:" + Base64.encode64("#{hmac_sha1.digest}")
end

def hmac_sha1
    @hmac_sha1 ||= HMAC::SHA1.new(@key)
end

def make_request(uri, header, method, body=nil)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    if method == "GET"
        req = Net::HTTP::Get.new(uri.request_uri, header)
    elsif method == "POST"
        req = Net::HTTP::Post.new(uri.request_uri, header)
        req.body = body
    elsif method == "PUT"
        req = Net::HTTP::Put.new(uri.request_uri, header)
        req.body = body
    else
        puts "Method not found"
    end
    http.request(req)
end

def get_almacenes
    make_request(
        URI.parse(@base_url + "almacenes"),
        {'Content-Type': 'application/json', 'Authorization': get_auth},
        "GET"
    )
end

def get_sku_stock_almacen(almacen, sku)
    make_request(
        URI.parse(@base_url + "stock?almacenId=#{almacen}&sku=#{sku}"),
        {'Content-Type': 'application/json', 'Authorization': get_auth("GET" + almacen + sku)},
        "GET"
    )
end

def get_sku_with_stock_almacen(almacen)
    make_request(
        URI.parse(@base_url + "skusWithStock?almacenId=#{almacen}"),
        {'Content-Type': 'application/json', 'Authorization': get_auth("GET" + almacen)},
        "GET"
    )
end

def move_product_to_almacen(product_id, almacen)
    uri = URI.parse("http://brocoli13.ing.puc.cl/storage/moveItem")
    http = Net::HTTP.new(uri.host, uri.port)
    req = Net::HTTP::Post.new(
        uri.request_uri,
        {'Content-Type': 'application/json'}
    )
    req.body = {productoId: product_id, storage: 'cocina'}.to_json
    http.request(req)
end

def find_product_out_cocina(sku)
    @almacenes_no_cocina.each do |almacen|
        products = JSON.parse(get_sku_stock_almacen(almacen, sku).body)
        return products.first["_id"] if products.length > 0
    end
    return nil
end

def product_in_cocina?(sku)
    return JSON.parse(get_sku_stock_almacen(@cocina, sku).body).length > 0
end

def fabricate_product(sku, amount=1)
    uri = URI.parse("http://brocoli13.ing.puc.cl/factory/requestItem")
    http = Net::HTTP.new(uri.host, uri.port)
    req = Net::HTTP::Put.new(
        uri.request_uri,
        {'Content-Type': 'application/json', 'Authorization': get_auth("PUT" + sku + amount)}
    )
    req.body = {sku: sku, cantidad: amount}.to_json
    http.request(req)
end

def fabricate_sku_recursive(sku)
    fabricable = true
    puts 
    puts_black "Fabricando [#{sku}]#{@productos_file[sku]["name"]}..."
    requeriments = product_requirements(sku)
    if requeriments.length > 0 # Si tiene requerimientos
        requeriments.each do |req|
            req = req.to_s
            puts "Requiere #{@productos_file[req]["name"]}"
            if product_in_cocina?(req)
                puts_purple "Hay #{@productos_file[req]["name"]} en la cocina"
                next
            end
            product = find_product_out_cocina(req)
            if product
                puts_blue "Moviendo #{@productos_file[req]["name"]} a cocina"
                move_product_to_almacen(product, @cocina)
            else
                fabricable = false
                fabricate_sku_recursive(req)
            end
        end
        if fabricable
            puts_green("Cocinando #{@productos_file[sku]["name"]} (Tiempo de espera: #{@productos_file[sku]["waiting_time"]} mins)")
            fabricate_product(sku, product_batch(sku).to_s)
        else
            puts_red "Faltan ingredientes para fabricar #{@productos_file[sku]["name"]}"
        end
    else # Ingrediente
        puts_red "Pidiendo #{product_batch(sku)} #{@productos_file[sku]["name"]} a la fabrica (Tiempo de espera: #{@productos_file[sku]["waiting_time"]} mins)"
        fabricate_product(sku, product_batch(sku).to_s)
    end
end

for skuToCreate in ARGV
    fabricate_sku_recursive(skuToCreate)
end
