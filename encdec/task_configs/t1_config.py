DATA_SPLITS_SIZES = {

    "train_dataset_1": {"validation": 1000, "train": 10000},
    "train_dataset_2": {"validation": 1000, "train": 10000},
    
}

split_infos = {
    "train_dataset_1": {
        "features": {
            "inputs_pretokenized": {
                "dtype": "string", 
                "shape": []
                }, 
            "targets_pretokenized": {
                "dtype": "string",
                "shape": []
                }
        }, 
        "num_shards": 1, 
        "seqio_version": "0.0.6"
    },
    "train_dataset_2": {
        "features": {
            "inputs_pretokenized": {
                "dtype": "string", 
                "shape": []
                }, 
            "targets_pretokenized": {
                "dtype": "string",
                "shape": []
                }
        }, 
        "num_shards": 1, 
        "seqio_version": "0.0.6"
    }
}