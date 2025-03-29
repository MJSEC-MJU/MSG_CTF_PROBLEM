# MSG_CTF PROBLEM

This repository contains a collection of CTF problems.  
Below is the list of problems with their categories, titles (linked to the problem path), and contributors.

| Category       | Problem Title                                                                                                                                                 | Contributor                                                                                                                                                         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WEB            | [I deliver your food sir](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/I%20deliver%20your%20food%20sir)                                             | [<img src="https://github.com/goldsimchoi.png" width="50" height="50" alt="goldsimchoi"><br><sub>goldsimchoi</sub>](https://github.com/goldsimchoi)              |
| WEB & Crypto   | [JMT](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/jmt)                                                                                              | [<img src="https://github.com/jongcoding.png" width="50" height="50" alt="jongcoding"><br><sub>jongcoding</sub>](https://github.com/jongcoding)                  |
| WEB & Crypto   | [Django_session](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/django_session)                                                                          | [<img src="https://github.com/jongcoding.png" width="50" height="50" alt="jongcoding"><br><sub>jongcoding</sub>](https://github.com/jongcoding)                  |
| WEB & Crypto   | [MD5¿¿¿¿](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/MD5%C2%BF%C2%BF%C2%BF%C2%BF)                                                                      | [<img src="https://github.com/MEspeaker.png" width="50" height="50" alt="MEspeaker"><br><sub>MEspeaker</sub>](https://github.com/MEspeaker)                      |
| WEB            | [excuse me, can I get a burger](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/excuse%20me%2C%20can%20I%20get%20a%20burger)                             | [<img src="https://github.com/rhkrskdud.png" width="50" height="50" alt="rhkrskdud"><br><sub>rhkrskdud</sub>](https://github.com/rhkrskdud)                      |
| WEB            | [CSRF_PROBLEM](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/CSRF_PROBLEM)                                                                              | [<img src="https://github.com/tember8003.png" width="50" height="50" alt="tember8003"><br><sub>tember8003</sub>](https://github.com/tember8003)                  |
| Reversing      | [MSG CTF Crack me](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/MSG_CTF_Crack%2Bme)                                                                      | [<img src="https://github.com/yunttai.png" width="50" height="50" alt="yunttai"><br><sub>yunttai</sub>](https://github.com/yunttai)                              |
| Reversing      | [Baby speak,,](https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM/tree/main/Baby%20speak%2C%2C)                                                                                 | [<img src="https://github.com/yunttai.png" width="50" height="50" alt="yunttai"><br><sub>yunttai</sub>](https://github.com/yunttai)                              |
                                       
---

## 서버 설치 단계
1. 시스템 패키지 업데이트 및 Docker 설치:
    ```sh
    sudo apt update
    sudo apt install docker.io
    sudo systemctl enable --now docker
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    docker-compose --version
    ```

2. 프로젝트 클론:
    ```sh
    git clone https://github.com/MJSEC-MJU/MSG_CTF_PROBLEM.git
    ```

## 가상환경 설정
1. Python 가상환경 설치:
    ```sh
    sudo apt-get install python3-venv
    python3 -m venv venv
    source venv/bin/activate
    ```
