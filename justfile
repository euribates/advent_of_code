
[no-cd]
encrypt:
    gpg --output input.gpg --encrypt --recipient euribates@gmail.com input


[no-cd]
decrypt:
    gpg --output input --decrypt input.gpg

dot := '.'

[no-cd]
test +options=dot:
    @echo {{GREEN}} "Testing" {{NORMAL}}
    python -m pytest . {{options}}
