
<table style="border: 1px solid transparent">
  <tr>
    <td>
<a href="http://talky.readthedocs.io"><img src="https://img.shields.io/badge/Wiki-%23000000.svg?style=for-the-badge&logo=wikipedia&logoColor=white"></a>
<a href="https://github.com/mraniki/tt/"><img src="https://img.shields.io/badge/github-%23000000.svg?style=for-the-badge&logo=github&logoColor=white"></a>
<br>
<a href="https://hub.docker.com/r/mraniki/tt"><img src="https://img.shields.io/docker/pulls/mraniki/tt?style=for-the-badge"></a>
<br>
    </td>
    <td align="center"><img width="200" alt="Logo" src="https://user-images.githubusercontent.com/8766259/233823991-cceaa05a-ff15-4796-a6bb-bcb3ee0d8859.jpg"></td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/findmyorder/"><img src="https://img.shields.io/pypi/v/findmyorder?style=for-the-badge&logo=PyPI&logoColor=white"></a><br>
      <a href="https://pypi.org/project/findmyorder/"><img src="https://img.shields.io/pypi/dm/findmyorder?style=for-the-badge&logo=PyPI&logoColor=white"></a><br>
      <a href="https://github.com/mraniki/findmyorder"><img src="https://img.shields.io/github/actions/workflow/status/mraniki/findmyorder/%F0%9F%91%B7Flow.yml?style=for-the-badge&logo=GitHub&logoColor=white"></a><br>
   <a href="https://talky.readthedocs.io/projects/findmyorder/index.html"><img src="https://readthedocs.org/projects/findmyorder/badge/?version=latest&style=for-the-badge"></a><br>
   <a href="https://codebeat.co/projects/github-com-mraniki-findmyorder-main"><img src="https://codebeat.co/badges/9b113098-d22d-498d-9c61-eb1e96c1311a"/></a><br>
   <a href="https://codecov.io/gh/mraniki/findmyorder"><img src="https://codecov.io/gh/mraniki/findmyorder/branch/main/graph/badge.svg?token=4838MSZNCC"/> </a><br>
    </td>
     <td align="left"> 
        Find My order,<br>
       a parsing package to find trading order.
     </td>
  </tr>
</table>

<h5>How to use it</h5>
<pre>
<code>
      from findmyorder import FindMyOrder
         fmo = FindMyOrder()
         msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
         order = await fmo.get_order(msg_order)
         #{'action': 'BUY', 'instrument': 'EURUSD', 'stop_loss': '1000', 'take_profit': '1000', 'quantity': '2', 'order_type': None, 'leverage_type': None, 'comment': None, 'timestamp': datetime.datetime(2023, 5, 3, 12, 10, 28, 731282, tzinfo=datetime.timezone.utc)}
</code>
</pre>


<h5>Documentation</h5>
<a href="https://talky.readthedocs.io/projects/findmyorder/en/latest/"><img src="https://img.shields.io/badge/Documentation-000000?style=for-the-badge&logo=readthedocs&logoColor=white"></a><br>
