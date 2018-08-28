import pytest
import readwritedata

def test_generate_csv():
    """_asdict() should return a dictionary."""
    t_task = readwritedata()
    t_dict = t_task.generate_csv("D:\GitLloyds\Python\python-app\raw.csv")
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected