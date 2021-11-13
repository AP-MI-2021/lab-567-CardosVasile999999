def do_undo(undo_list, redo_list, current_list):
    """
    Face undo la ultima comanda
    :param redo_list: lista dupa redo
    :param current_list: lista curenta
    :param undo_list: lista dupa undo
    :return: modifica lista eliminand efectele ultimei comenzi
    """
    if undo_list is not None:
        redo_list.append(current_list)
        return undo_list.pop()

    return None


def do_redo(undo_list, redo_list, current_list):
    """
    Face redo la undo
    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista inainte de undo
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    else:
        return current_list
