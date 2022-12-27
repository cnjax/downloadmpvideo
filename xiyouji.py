# -*- coding: utf-8 -*-
# Generated by Selenium IDE

import time

import json

from bs4 import BeautifulSoup
import re

import requests


class TestAll():
    def start(self):
        urls="""http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=2&sn=02900ac784e377dc4d882393088d1592&chksm=888f77f8bff8feeef4458432065665c95be1e6729509556ddcbd57f83058f5cea2ac604024a9&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=3&sn=e7dd3cd4420a6f1061e277f0434cf7b1&chksm=888f77f8bff8feee4b7f4876fbb6761da7959382434efa69846b1519d1ec070537c7d9ec28ae&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=4&sn=74a1c240da11ee219318e2474c5aa7cb&chksm=888f77f8bff8feeedc45f8ba15a43317ae336cb6bdcae59e832dc71765ee992ea59e66bbbc20&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=5&sn=b098382cba56019fff229ec133c7d324&chksm=888f77f8bff8feeebb08d43889946981a9cd58daac83eed9a5504f6260ff4664ac3f8a048973&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=6&sn=b12ca28cf0b3e2fef022d87822a7d067&chksm=888f77f8bff8feee22fed2ccd3a0c2b97c1fc9071d29bf0b176cd7ce1c606e29c2f6dfd16532&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413317&idx=7&sn=af29372d8757d875e5bc36454da0eff4&chksm=888f77f8bff8feeeb56f214acdb3133b5530895ff3dca38b5534a3506263727114ebe226b578&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=3&sn=b4e0669ac6d087d431f2cefffb9ed8e4&chksm=888f773bbff8fe2de2cef34e8ce0a84e91f0a913efb676418724bf90b0b6bcca61519ed0484e&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=4&sn=c1e5161c2ed26097748e28151e015ab7&chksm=888f773bbff8fe2dfa2bf4223e40fc6b42d2025c429048ec4e0d0bee305cd3bb94159a02e431&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=5&sn=4066e055e22aa14464f17cf4740a0a07&chksm=888f773bbff8fe2de2c017748408c9fa8d93a5624beae00241c6ea0f4a9f98c62deb9ca7d8af&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=6&sn=73cc4a1529bc630665b4e57f33912688&chksm=888f773bbff8fe2d13f6afb3717e16260f563b5e824a300b91e6ea26521c365c3ded50e2ca74&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=7&sn=89f2b57eee6693e6a18e3030aa63c701&chksm=888f773bbff8fe2dea391575694958a67d3764cf7b5f84cb6a077f641bf632727e67ec750010&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=8&sn=6ffc66f7265ea60ece5580a3dc360de4&chksm=888f773bbff8fe2dc6f54dd42ab166726c088a54f8ac146724c208f710a00fce3b30bafe0d1c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=1&sn=c98b50e68976af87f7571169bb808f53&chksm=888f7728bff8fe3e7847fed7272bdeac787ded28fe489594129da7a52c34f0177cca8e6db3d5&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=2&sn=3776ee897a37bf3af4054f50dade536a&chksm=888f7728bff8fe3e7219e18ee0c25ba244ca763a9ffcc06b0e351b84ad5944119381592309bd&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=3&sn=cfbfc8951ee95ee25a3309301fa8aefb&chksm=888f7728bff8fe3ee6cd63e339d7732bbd7834d2221494b0304b6f6eafcd0f12fd38c3f8fb85&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=4&sn=6fb28bbc50897d3c26face9d7e0d6461&chksm=888f7728bff8fe3e98807a94f5a4be680b93e95042b982450b09e157345ed655c2993a86a6aa&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=5&sn=eb7e31b8350d27b2fc7f90f7415f4d0c&chksm=888f7728bff8fe3ebb5b63b168bc42fabced8a509f4800db45438fa91ba6901c02750b392f97&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=6&sn=e1a54bbf7989d48eed9d028f88aa70c7&chksm=888f7728bff8fe3e5476eafa3e4aa65d6c2948ed97d61b3d9d5920ebd31a8424ff5e9d59efdf&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=7&sn=5ff739761756190e35de7f61b55d8884&chksm=888f7728bff8fe3ee4cecbceca6a3ba4d5033cb50c1af297bb0ce953c3b948746f67f4425854&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413269&idx=8&sn=5eacd3b4b72500e78a147db98a065d6a&chksm=888f7728bff8fe3ec2206e6536c8612017ecdc7bdac7e29ccd77392d42a0eaf10fa2f1811448&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=2&sn=6175742333aa605103a99a38f9203c0e&chksm=888f7203bff8fb15b2e2e8bb29395f3c3cafe7f1c34dd8c37e47185c0e481951f02ddf40f4d8&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=3&sn=dad40f4109e334bd89cd82a9a05a2f81&chksm=888f7203bff8fb150b28e37243c9ca7c58e5e44c3359bec33fa3cb02ecfc5da1dc61a3816f8f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=4&sn=dfedca00689bdd9e3b6e0a0ee620a79e&chksm=888f7203bff8fb15d66cba1b2ab04deb5a8dbf2520a92c298ec7a2328339e258409b89631a94&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=5&sn=bd8605dbacac8137d5c9fa58f51fd3f2&chksm=888f7203bff8fb1530f21ed5676683cf6ec1c266d5eeb659e497dbb1198fc2dbbee083178478&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=6&sn=cba80bb04b41c97888a8f5ecd5047f01&chksm=888f7203bff8fb154a22ec886279ac5f329cbd4018148334993b5be75619312af688afbd03a6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=7&sn=9a654c1f7f154e359f758c32f3d6f3a7&chksm=888f7203bff8fb1598a93e3281d274e21078adacef69d307af50e53a475ce05b50693d68cad0&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412542&idx=8&sn=df2def6c5c9de038c52e9d70f8b95184&chksm=888f7203bff8fb15519c5a93e625ad60879911786e3ffec3750f01bdbfe626e8cf8561082525&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=2&sn=cbf80e8832f3e773ab3f6156c17a0087&chksm=888f71cfbff8f8d991977e2b38a12c150de90fee29df3a0e9d372365421b28ccdfb3bf4c5126&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=3&sn=4e2b945c8d712e895183e7f840796811&chksm=888f71cfbff8f8d947781ccc98d592978a82c1a8ef0b54134cd6df69bdc3ccaa82669b733506&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=4&sn=d38b1f7553875b81cc11f83a0fc587d5&chksm=888f71cfbff8f8d9fb1521238e05aeff01e26c8271c51f86fbb18cd503f7b32b054aeea37db3&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=5&sn=7fffbb1fa2c023b1b5ecb4cb5b6058e3&chksm=888f71cfbff8f8d98f124667ace440b1d725e7704396190d699882570faed3d08597a521c1ad&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=6&sn=1288c58452d5181a27d9ee5714bfa25b&chksm=888f71cfbff8f8d93ef7ec404ce332cc68d7fcb7ba95f998c694ebfdd3ca7a585b3a7b01ddd5&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=7&sn=4294330f3b5ed243a43ea0a6edd694a2&chksm=888f71cfbff8f8d9a3fda64995654f0a559b75afac873eb2399af984fa2acec2c15d53362439&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412850&idx=8&sn=2240b100a50b05be90e2605c44087497&chksm=888f71cfbff8f8d9567be944a839f6d89d01a088a6ce331d5d595bacd4326efd2a3a22a97a28&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=2&sn=4eba2c7415299277fac0c9b88ca37b1b&chksm=888f71bebff8f8a823c01ff31ac14e4c0165700b1a6484d900d30d3e9e0921b72d52ada6319d&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=3&sn=d77b6439a29d15661ddec9b372c8413f&chksm=888f71bebff8f8a870e30e991e6408f3899e8b9692679b52863c4c009874fb0bd6848270b303&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=4&sn=41b03e3aa1b5a36cbe68f7d202eb8138&chksm=888f71bebff8f8a88f810e373ae770145f4ba419a723d5c2c2afa0f433cae8c8139339613f91&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=5&sn=a778a4655d64db76b14e298175a03b9c&chksm=888f71bebff8f8a8b5f236c6622d8e05cdd2e6e622c33e0f8f4f8b9ca020e6e9a63879796b06&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=6&sn=70f20f2b626d68d1c85b8e10456d2cb4&chksm=888f71bebff8f8a80ecda62191663978107bb0908b886b67e849f3d770efedad71c75c25cbf7&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=7&sn=4cc6eaba91a2c5588d6c448cd1d8ff8d&chksm=888f71bebff8f8a88d2b5d1cb81bad431c1b05d9e21256f936b7d3503d28f24307185d710182&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412867&idx=8&sn=3d95fdb0acd8d4cd2c3e94a9e1475c05&chksm=888f71bebff8f8a860b94ec4117e95c7cd474b61d6467481e5dfe53f34d60d5b344381b245f6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=2&sn=c10e657c43ce8bf465f496dba34390d7&chksm=888f718fbff8f899b9df6cffc5f35712c620a841149d83e9b3e4e5531f34576fb8d446562c8c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=3&sn=f1205f6a4ab1fe9e01051275c40a41a5&chksm=888f718fbff8f8994781a95da440846c7e9712b19d95dca5d1ccb1c1718026200d176427e252&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=4&sn=20403e96df965cbe1aa2df8ca717cd7f&chksm=888f718fbff8f8997176553c95ad0247a2dbd89cf87593a6458d88af580952c651e0295425f7&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=5&sn=e17bd51e35092abd6339b2f374992ae9&chksm=888f718fbff8f899fddefc313e698a6f4b754e336081a6f7b3798af23862b8ad5b7541dffccb&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=6&sn=a369618022f6b6994d206add55923328&chksm=888f718fbff8f8993c84a6d1d55cce04a0fc15c64a3e93030577640cd246878f693c082f4b7a&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=7&sn=321b777e9c409a747a3ea55c0c144a71&chksm=888f718fbff8f89956b917b0b1ab44ba3486cf6baaf25208b54abd0a6cd7a9a1461b5cd6024b&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412914&idx=8&sn=186c0b102342952efe1d662eb6d279f5&chksm=888f718fbff8f899a570ee1f03bdf06c0b44c91010f24e2f4b6aacee0f41226c3e4ba46ec315&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=2&sn=098ea37649980fabfb301b3ffa25763e&chksm=888f707fbff8f96958feaf6b6e3fa40e8090ca5b8fa53f971702bebfd560a9b04d8cab5dcbb6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=3&sn=7213613c84527a2dad399c6c8f9201bd&chksm=888f707fbff8f969e3625b41c1f45229d307f2aa46123cccb620e4ceefbeefc14924e6a88c59&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=4&sn=3e52cf45b306db55b4f05ddd2cc0e644&chksm=888f707fbff8f96959ca6e8746047f61220ada5c82f92f70b067025443d67e8923c1cb3e7c19&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=5&sn=9fd84480617618921c62e8a4bb1d2bb7&chksm=888f707fbff8f969aa856b36464d8723431be6873ee971e9bb049ec0d95f07410944f9d20fef&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=6&sn=d3bc658a70a5731c6d531e6878775d8a&chksm=888f707fbff8f969a09757b1eb4fded91c60f17bccdd0833873a211348bc1621409b7616e64c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=7&sn=b08388f39048eeabb3a21eb21c167c10&chksm=888f707fbff8f9694e6ccb000152f8629a08acb32e32a549137cee2c5a24de6ec3130d7482c3&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648412930&idx=8&sn=869361290bf5f48c94fc5739015c327f&chksm=888f707fbff8f9698463d8f8fe11d73c0737e96cec403f1750d8debec94e564db8d7955429fe&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=2&sn=43552da501271d875c153de3244c01ab&chksm=888f70f1bff8f9e714c64a48e16a4e69675733288a830d1c5c2a7530db92fb5c43cf83004492&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=3&sn=8b519d55b2c50227d95c9e7fc63ac0c1&chksm=888f70f1bff8f9e708b8d0f36d9711595beb9adf5406c9f94afde6dcb0cbd1136045c12d50e9&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=4&sn=62b512e5316ded3c5df42cc2872a93ec&chksm=888f70f1bff8f9e7b5a36b94a6a4530f90dc4de539b4b264b94cba590037004497e6e9b9112c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=5&sn=bd7eab78dfdee0ef9de1e198196312e1&chksm=888f70f1bff8f9e74d0c1367ea9f81172a340c0204e50bce6339c280a76329415e660a5f2b37&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=6&sn=7ca0fb3b54be3dc97d0ccb6507de0b49&chksm=888f70f1bff8f9e79ccb28e8a82621852557772c0921bc284a26e9d5749a6d1c44f496aefc62&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=7&sn=c667802c76215ed75d64f94d7452e431&chksm=888f70f1bff8f9e76a33eaf5a239d9f3cd4ca7235710ba734720fcc50215023791083e03b7a3&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413068&idx=8&sn=492715ee8042bb6b89a038d0ef327c01&chksm=888f70f1bff8f9e7a5cc02be412da7583872be9768e0e8db1d422631dbca3785da5f94427b9f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=2&sn=c22d757afeb859b595574f95cbb1aa8d&chksm=888f70e1bff8f9f759ecc0179558fbcbd4fce5980bde1f5d826e9d1a21d9bc0b73468db36394&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=3&sn=326fbbe4ec747eb2ff4604b6ac0d393a&chksm=888f70e1bff8f9f71af2c6c1b23402747403181c867989f3fb637557ceeb9fba7db0d871416d&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=4&sn=444183a0dc7e08f49e90fc9747b61ff6&chksm=888f70e1bff8f9f71fbecebf6f53dfde8f4a5660f94dd6999439a35fafe7abc5485dc2a14fb8&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=5&sn=03328741b4d9fee3373917a20356e24e&chksm=888f70e1bff8f9f7d1c3d05e9c3449468d918b1dc414f091c274b8eb6129593209dbc32d6016&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=6&sn=7e07af5d580e5d4b6e412d87bfbce858&chksm=888f70e1bff8f9f7b1a5bbfa5fee027d18e5542ed0d28dba24ba46e4d686140a1422458448c4&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=7&sn=fa97af684e7a5a6f084098226145c4b8&chksm=888f70e1bff8f9f773517a48233835c0d3b6d80c89caad3d34281ea61573bd0fe9e7798cb1c6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413084&idx=8&sn=4b17f31e3c021faa98c3629cc4609de5&chksm=888f70e1bff8f9f7e0aa2ffe5edd6a91eca1197aa6354e6dcff855e737ad594f2fb8bec7261a&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=2&sn=0c8e2963315548c6c918f6b51b7492aa&chksm=888f70a7bff8f9b176665b9c49ba77733e9be01a63272910a5d533abef68efa9d1ac78bc92d6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=3&sn=df170161c8ac6c00b44f4007e87cc458&chksm=888f70a7bff8f9b1f69bcf99d6c461722ab29a028a29a8d4a45ad03e00bb1fdf9c17901ecd84&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=4&sn=47b894ad7bd9cd600606741d5fed5509&chksm=888f70a7bff8f9b1b837365e8ef7304dc07e9bb57ff2ad8ae9c4ec2c5df820d860222a908bbf&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=5&sn=6d8bcada50249f83864ee66e7dfa7ad8&chksm=888f70a7bff8f9b1cc74fdbc2ae6463291fa0fcc395807b8630c6401a4c9e3066852634ea0aa&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=6&sn=75b8728cf84df1e31c20df823cd9b991&chksm=888f70a7bff8f9b129e4303e19d302c156da868a534ce7d9220965f6ada3d066f6e73e514cb2&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=7&sn=38260e0a7f8b5b27e7d08d0e80b0c195&chksm=888f70a7bff8f9b11c415f31807143da4f4d452cbc1bd450541757b8c0c39ddb989ae1ae7d2c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413146&idx=8&sn=e0226390bbd22868c0623c50c006a9b8&chksm=888f70a7bff8f9b151961f2a6eb918228b93766a09a017d74aa31056923a991a3d9e185129db&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=2&sn=02b1d5dfe7d62296a6ac1abe748f9ccd&chksm=888f709abff8f98cf537282ff63af0819fa3f7bbe22235f18e1a1ca63f91fff565d72aa50d5c&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=3&sn=2ddf309e1b2aed7788a960f0aeb1f989&chksm=888f709abff8f98c2b9670612e75f1df60b505693b2344ce47fd5ac393568b3433480cd5796a&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=4&sn=a7f38961c46c04470980d4a5b43e7957&chksm=888f709abff8f98c3c8c34ea43cbb5694ea0106250a00514e686389a4a176fc325e8c133d60f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=5&sn=dfc9c20edd4595b9bded56c39c78d678&chksm=888f709abff8f98ca8be5bc6b2edcb67137add9d960aecb703337f2974cbd0945cfb8af13687&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=6&sn=5adc549bf556197423c0843a20120380&chksm=888f709abff8f98cb6235947740a7a267b07812eaa6618e7e20f0ef2599b9cb5f0f3f60b0ed7&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=7&sn=490c7849666706a5ddb6914a49599aec&chksm=888f709abff8f98c3b53430aafc9184f4a2cd1da0ad4239689e78fcd494977237c146747edb6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413159&idx=8&sn=f5b46c3f4b24faae1d7eeaf04e9536b5&chksm=888f709abff8f98ce3a1f78e3c946060a5d36c852e5a3a4c8c01e426c568f7608516a64e74be&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=2&sn=b59e10d17879ff32a575345ae4b4f761&chksm=888f708fbff8f9999ed9c2a9ddf3bf69f447e747e8b60aac7bb501eb5b01f1118b8373166ce5&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=3&sn=81782a39c532b3255f89cf7001c635e7&chksm=888f708fbff8f99907ee30cf9cb7d8b6daecf4d3160ab07e04e817d59cb3413367ac528588bf&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=4&sn=3ae4ab4279ba734bd5806d616d8ae2f1&chksm=888f708fbff8f999edc8814c4ad427e39fecb5b3718b47df0c826c8810c3d2cc4d6bef6fc505&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=5&sn=23d3d8c916503eb710a8a015fddd3a3b&chksm=888f708fbff8f999b8b3cc701a86cd7c1ea2b7858f7a7d950fa784c539e349bc17bc4c26fb7f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=6&sn=f3f7c23f34e561aac2085044dcbe3f41&chksm=888f708fbff8f9992e984c02169a0608684d6c0f24c66e13be7e73698cda75fcc75dd49bf928&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=7&sn=8964ed14796306ed4b01c99cceebaac3&chksm=888f708fbff8f999c4f12707bea5b527bf389133cea489462aa3973b5e46e3dfa0cfa04c79a6&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413170&idx=8&sn=23b901ca72d29e1be3ecdb5b0a32a20a&chksm=888f708fbff8f99940c85e88d267c5316824fe38dba0f3383c736c9ab25713f0f634074c1728&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=1&sn=2af84f1010ebc9be9f83d134e82562a9&chksm=888f7081bff8f99774f23c0bcc5364473242eaf014ac63e887120361c090c2b6401db0a4eb1b&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=2&sn=4a662ce4fb5b602cf4d2bf1585f513b3&chksm=888f7081bff8f997c31cd2a14c6e90644ac82243498d1994e9955505223ca63a3c4601275d19&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=3&sn=dd649f3face00a7afd63219193ad4e74&chksm=888f7081bff8f997f514e8fbf30cb730af7a5e593f87194637b565d8ce4d8358c7d7b2e80388&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=4&sn=69e1f2a282e586c8f7fa5a813f4fffb2&chksm=888f7081bff8f997544c5eda50cddc28980a9b514ea38ebef9ee3ed913deb3e3893aaa79a966&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=5&sn=1512737a033a8fadf2e66739a3ff4e7b&chksm=888f7081bff8f9973723847721e668cd626a173f9215b4cc98fa07602a86721239e9664d5138&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=6&sn=be6de6c496b17afa4d1459f3a561c97a&chksm=888f7081bff8f99747f1615148833c0cf36cbd29ac505f705356ec843710700080649b3c1855&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=7&sn=43711232aa518f81ae96bc3d6afa67b1&chksm=888f7081bff8f997f0723af85e8b713c27b673c8eeefbe36530d7f4c1bad746d7585e13f2363&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413180&idx=8&sn=f19c333c051318cbec1f5f15ca788e7c&chksm=888f7081bff8f99707662d9222a6d0ea44863d4e9a7f4a6584ff49ac82c929ac7388ccf0bdfa&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=1&sn=1f384c803bc66198d570b2c15a206cba&chksm=888f7741bff8fe578f4c74e4b446de3e8df2d2e8c82d3805349b0c5995528c4629d3da29a9d1&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=2&sn=606466ac94bf9baccc3be8f3046e8b23&chksm=888f7741bff8fe57a75f830f6915c16c5b53e5f8d3a0141f60e9d7463eced6d975e892ad4851&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=3&sn=f852a1dfbb876d2de3cb7eb2b93368a4&chksm=888f7741bff8fe57f8f6494e24f04a71ece24ff507a71e58151c99f5e50b9f3782e996126c0a&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=4&sn=23b4bbfcc416c068dc752f7ad2d5f73e&chksm=888f7741bff8fe5702ffce53234196afd791179db8d510840b84412281df5c6e3b341e31aa1d&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=5&sn=bb3db799f651fc40390df03a52d3e80f&chksm=888f7741bff8fe57bedbfb7bafa1dbf19a66f8769b53b3eac1931a8126b4cd9af54c33651b45&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=6&sn=ae655296971911cbd8268e8e4193c663&chksm=888f7741bff8fe57e937c56b212af2ccd1384cb0ee557f58c726d3856956c6189144296d2f9f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=7&sn=bb9213a8056907a4af5fc052277695f2&chksm=888f7741bff8fe57023bd5118752c90ae8f34e6250be54afc01845c30ba7d9132ad3f331cb4b&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413244&idx=8&sn=a8e3f52f8a3f15f77cb5ef8cf93c1d23&chksm=888f7741bff8fe5706739ee3dcd3f80f615f68ac88fadf07e7fb600bececad0fbe42c1c0528f&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=1&sn=0c50d3c430d6fbb38f1f795797189357&chksm=888f773bbff8fe2dc6520227eb024c06290f2db279ca5f23485b0b7d31d5b5dad964a84955bc&scene=21#wechat_redirect
http://mp.weixin.qq.com/s?__biz=MzA5NzQ3NDA2Ng==&mid=2648413254&idx=2&sn=d62fb4a1283472ce8e9ac4ada34f8923&chksm=888f773bbff8fe2dfd2fe6eeabeb015baef9e3071b26584acaed4603b807e1bf7da4622926e9&scene=21#wechat_redirect"""


        # for url in urls.split("\n"):
        #     print(url.strip())
        vurls=[url.strip() for url in urls.split("\n")]
        # vurl="https://v.qq.com/iframe/preview.html?width=500&height=375&auto=0&vid=p0909svx8fq"
        # print(vurl.split("=")[-1])
        #


        log=[]
        i=1
        with requests.Session() as r:
            for vurl in vurls:

                response=r.get(vurl)
                soup = BeautifulSoup(response.content, 'lxml')
                ttag = soup.select_one(".video_iframe")
                vid=ttag.attrs["data-src"].split("=")[-1]
                if vid.startswith("wxv_"):
                    ret = self.getmpurl(response.text, i)
                else:
                    ret=self.gettencenturl(vid,i)

                if ret is not None:
                    log.append(ret[1])
                    with open("qqvideo.txt","a") as f:
                        f.write(str(ret[0])+'\n')
                    print(ret[0])
                time.sleep(0.5)
                i=i+1

        print(log)


    def getmpurl(self,result,index):


        #result = requests.get(url).text
        biz = re.search(r'__biz=(.*?)&amp;', result)[1]
        mid = re.search(r'mid=(.*?)&amp;', result)[1]
        vid = re.search(r'wxv_(.*?)\"', result)[0].replace('\"', '')

        video_url = f'https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz={biz}&mid={mid}&idx=1&vid={vid}&uin=&key=&pass_ticket=&wxtoken=777&devicetype=&clientversion=&__biz={biz}&appmsg_token=&x5=0&f=json'

        url_info = requests.get(video_url).json()['url_info'][0]['url']
        return url_info,index

    def gettencenturl(self,vid,index):
        print(f"vid json is getting: {vid}")
        template_url = f'http://vv.video.qq.com/getinfo?vids={vid}&platform=101001&charge=0&otype=json&defn=shd'
        with requests.session() as r:
            res=r.get(template_url)
            if res.status_code==200:
                try:
                    response=res.text
                    json_data =response[len('QZOutputJson='):-1]
                    json_obj = json.loads(json_data)
                    download_url = json_obj['vl']['vi'][0]['ul']['ui'][0]['url'] + json_obj['vl']['vi'][0]['fn'] + '?vkey=' + \
                                   json_obj['vl']['vi'][0]['fvkey']
                    video_name = json_obj['vl']['vi'][0]['ti'] + "." + json_obj['vl']['vi'][0]['fn']
                    return download_url, video_name
                except Exception as e:
                    print(e)

            else:
                print(index)
                print(template_url)
                print("fail request",res.status_code)
                return None

    def createm3u(self):
        with open("qqvideo.txt") as f:
            urls=[url.strip() for url in f]
            i=1
            f=open("qq.m3u","a")
            f.write("#EXTM3U\n")
            for url in urls:
                f.write(f"#EXTINF:0,第{i}集\n")
                f.write(url+"\n")
                i=i+1

if __name__ == '__main__':
    t=TestAll()
    t.start()
    t.createm3u()

