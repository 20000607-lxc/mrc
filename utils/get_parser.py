# encoding: utf-8
import argparse

def get_parser() -> argparse.ArgumentParser:
    """
    return basic arg parser
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_dir", type=str, default="datasets/ace2005", help="data dir")
    parser.add_argument("--task_name", type=str, default="ace05")
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
    parser.add_argument("--mrc_dropout", type=float, default=0.1,
                        help="mrc dropout rate")
    parser.add_argument("--bert_dropout", type=float, default=0.1,
                        help="bert dropout rate")
    parser.add_argument("--weight_start", type=float, default=1.0)
    parser.add_argument("--weight_end", type=float, default=1.0)
    parser.add_argument("--weight_span", type=float, default=0.1)
    parser.add_argument("--flat", action="store_true", help="is flat ner")
    parser.add_argument("--span_loss_candidates", choices=["all", "pred_and_gold", "gold"],
                        default="all", help="Candidates used to compute span loss")
    parser.add_argument("--chinese", default=False, action="store_true",
                        help="is chinese dataset")
    parser.add_argument("--loss_type", choices=["bce", "dice"], default="bce",
                        help="loss type")
    parser.add_argument("--optimizer", choices=["adam", "sgd"], default="adam",
                        help="loss type")
    parser.add_argument("--dice_smooth", type=float, default=1e-8,
                        help="smooth value of dice loss")
    parser.add_argument("--final_div_factor", type=float, default=1e4,
                        help="final div factor of linear decay scheduler")
    return parser