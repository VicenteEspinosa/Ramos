CarrierWave.configure do |config|
    config.fog_credentials = {
        provider: 'AWS',
        aws_access_key_id: 'AKIAIFSWR6XGHB33WBKQ',
        aws_secret_access_key: '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',
        region:                'us-west-2'
    }
    config.fog_directory = "bucket-proyecto"
    config.storage = :fog
    config.fog_public     = false
end