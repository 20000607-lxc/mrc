# encoding: utf-8
import argparse

def get_parser() -> argparse.ArgumentParser:
    """
    return basic arg parser
    """
    parser = argparse.ArgumentParser(description="Training")
    parser.add_argument("--data_dir", type=str, default="datasets/ace2005", help="data dir")
    parser.add_argument("--device", type=int, default=1)
    parser.add_argument("--percent", type=int, default=10)
    parser.add_argument("--bert_config_dir", type=str, default="bert-base-cased", help="bert config dir")
    parser.add_argument("--pretrained_checkpoint", default="", type=str, help="pretrained checkpoint path")
    parser.add_argument("--max_length", type=int, default=230, help="max length of dataset")
    parser.add_argument("--batch_size", type=int, default=12, help="batch size")
    parser.add_argument("--lr", type=float, default=1e-5, help="learning rate")
    parser.add_argument("--workers", type=int, default=2, help="num workers for dataloader")
    parser.add_argument("--weight_decay", default=0.01, type=float,
                        help="Weight decay if we apply some.")
    parser.add_argument("--warmup_steps", default=0, type=int,
                        help="warmup steps used for scheduler.")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float,
                        help="Epsilon for Adam optimizer.")
    return parser