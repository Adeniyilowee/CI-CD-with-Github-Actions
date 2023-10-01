import pytest
from slapping.slap_that_like_button import LikeState, slap_many


def test_empty_slap():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_single_slaps():
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input, expected", [('ll', LikeState.empty),
                                                  ('dd', LikeState.empty),
                                                  ('ld', LikeState.disliked),
                                                  ('dl', LikeState.liked),
                                                  ('ldd', LikeState.empty),
                                                  ('lldd', LikeState.empty),
                                                  ('ddl', LikeState.liked)])


def test_multi_slaps(test_input, expected):                         # this is making use of the parameterized 
    assert slap_many(LikeState.empty, test_input) is expected       # variable (test_input and expected) set above by pytest
                                                                    # it makes it possible to run multiple test without canceling even with errors



@pytest.mark.skip(reason="regexes not supported yet")               # this is to skip a function you have not developed yet
def test_regex_slaps():                                             # hence, its good to use github tox so that it's updated
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail                                                  # for an expected fail, use x.fail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():                                            #  this values will fail if a values error is not raised
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, 'x')


@pytest.mark.xfail                                                  # This is a fixture for database defined in 'conftest.py', so pytest identifies it
def test_db_slap(db_conn):                                          # thus can be used for all functions that requires db_conn   
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):                                     # This is a fixture defined in 'conftest.py', so pytest identifies it
    print("hello")                                                  # thus can be used for all functions that requires capture_stdout
    assert capture_stdout["stdout"] == "hello\n"




# Needed to install package
# 1. pyproject.toml : its a config file for pytest and mypy
#                   :


# 2. setup.cfg : its a config file for storing all other metadata, like name etc
#              : it also provide config file for flake8


# 3. setup.py : two lines of code, thats all
#             :

# What to Run
# pytest
# flake8
# mypy src


# Git process
# git init
# git add --all -- ':!pytest_env/*'     #  add all files except a folder with everything inside. hence /*
# git status
# git commit -m "First testing project commit" # copy from http when git repo is first created
# git push -u origin main   # indicate -u origin main whhen done the first time or when you want to push to s specific generated branch
######### after wards
# make changes
# git add .     # gitignore knows what to leave out now
# commit and then oush 




# def test_many_slaps():
#     assert slap_many(LikeState.empty, 'll') is LikeState.empty
#     assert slap_many(LikeState.empty, 'dd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert slap_many(LikeState.empty, 'dl') is LikeState.liked
#     assert slap_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ddl') is LikeState.liked
