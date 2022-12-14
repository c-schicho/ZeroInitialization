import torch
from torch.utils.tensorboard import SummaryWriter


def write_train_summary(writer: SummaryWriter, model, loss: torch.Tensor, global_step: int):
    writer.add_scalar(tag="train loss", scalar_value=loss.cpu().item(), global_step=global_step)
    for name, param in model.named_parameters():
        writer.add_histogram(tag=f"trainable parameter {name}", values=param.cpu(), global_step=global_step)
        writer.add_histogram(tag=f"gradient of trainable parameter {name}", values=param.grad.cpu(),
                             global_step=global_step)


def write_validation_summary(writer: SummaryWriter, loss: float, accuracy: float, global_step: int):
    writer.add_scalar(tag="validation loss", scalar_value=loss, global_step=global_step)
    writer.add_scalar(tag="validation accuracy", scalar_value=accuracy, global_step=global_step)
