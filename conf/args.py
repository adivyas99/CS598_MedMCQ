from dataclasses import dataclass


@dataclass
class Arguments:
    train_csv:str
    test_csv:str 
    dev_csv:str
    batch_size:int = 16 ##Finetune this parameter to improve model accuracy
    max_len:int = 192
    checkpoint_batch_size:int = 32
    print_freq:int = 100
    pretrained_model_name:str = "bert-base-uncased" ##Switch between different models to test
    learning_rate:float = 2e-4 ##Finetune this parameter to improve model accuracy
    hidden_dropout_prob:float =0.4
    hidden_size:int=768 ##Finetune Hidden neurons to improve model accuracy
    num_epochs:int = 5 ##Training over differnt epochs can impact accuracy
    num_choices:int = 4 ##Fixed number of choices to get the output
    device:str='cpu' ##Switch between "GPU" or "CPU" based on your machine
    gpu='0'
    use_context:bool=True