import random
import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError
from telegram import (
    Update,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import CallbackContext

import HachiBot.modules.hachi_strings as hachi_strings
from HachiBot import dispatcher
from HachiBot.modules.disable import DisableAbleCommandHandler
from HachiBot.events import register


@register(pattern="^/joke ?(.*)")
async def joke(event):
    await event.reply(get_joke())


@register(pattern="^/insult ?(.*)")
async def insult(event):
    m = await event.reply("Generating...")
    nl = "https://fungenerators.com/random/insult/new-age-insult/"
    ct = requests.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"{cm}")


@register(pattern="^/url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.reply(
            "**Shortened url**==> {}\n**Given url**==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await event.reply("`Something went wrong. Please try again Later.`")


AD_STRINGS = (
    "_*kembali dengan versi terbaik, karna di sini aku masih menunggumu,masih tentang kamu*_",
    "_*healing terbaik jatuh kepada rebahan, jalan jalan dan makanan enak*_",
    "_*sorry I'm not a perfect person like you, also not arrogant like you,and it's not something that requires me to be jealous.*_",
    "_*maaf aku bukan orang yang sempurna sepertimu, juga tidak sombong sepertimu, dan itu bukan sesuatu yang mengharuskan saya untuk cemburu.*_",
    "_*jika kamu gagal menjadi orang sukses, berarti kamu sukses menjadi orang gagal.*_",
    "_*Aku tidak tahu dimana ujung perjalanan ini, aku tidak bisa menjanjikan apapun. Tapi, selama aku mampu, mimpi-mimpi kita adalah prioritas.*_",
    "_*sejauh apapun kamu melangkah pergi,dan sekeras apapun usaha kamu untuk ninggalin aku,aku ttp bersifat baik menerima kamu,krna kamu rumah bagi ku.  -zifaa*_",
    "_*ya Tuhan kalo emang dia jodoh orang lain, maka jadikan lah aku orang lain itu ehehe*_",
    "_*kurang2 in ngomentari fisik orang dia berusaha buat selflove tapi mulut anj lo gampang bngt bikin dia insecure. *_",
    "_*kenapa kakinya ayam 5? sebab i lope you.*_",
    "_*If I'm still sane by the time I finish their training it'll be a miracle!.*_",
    "_*UDAH PRENJON DI GHOSTING, MAMPUS!*_",
    "_*Bersamamu sudah terlalu banyak syair yang berkata-kata, hingga tidak ku sadari ada cinta yang terbuang sia-sia.*_",
    "_*setiap manusia memiliki kekurangan nya masing masing.jika semua dilihat dari kekurangan dan menjadi alasan untuk meninggalkan, maka sempurna menjadi kata yang tidak pantas diucapkan.*_",
    "_*Memiliki hidup yang lebih baik itu adalah pilihan antara mau terus mencoba atau mau terus mengeluh.*_",
    "_*pasipasipaga:(.*_",
    "_*aku ga akan pernah maksa kamu untuk selalu sama aku, kalau kamu udah ngerasa ga nyaman lagi silakan pergi cari yang bisa buat nyaman kamu kembali.*_",
    "_*never force yourself to be perfect, find a place where your flaws are accepted.*_",
    "_*jangan pernah memaksa dirimu untuk sempurna, carilah tempat dimana kekurangan mu diterima.*_",
    "_*“Kenapa kita selalu berharap padahal kita tau akhirnya pasti terluka”.*_",
    "_*kadang kita merasa udah nemu orang yang tepat di waktu yang tepat , tapi tepat buat kita belum tentu tepat buat dia*_",
    "_*Beberapa orang bermimpi untuk sukses, Sementara orang lain bangun setiap pagi dan mewujudkan nya.*_",
    "_*apapun yang terjadi tetap lah menajadi beban orangtua.*_",
    "_*kalau mau mencintai itu jangan cuma pake hati, tapi logikanya juga dipake*_",
    "_*ayo bertemu lagi dikehidupan selanjutnya sebagai pasangan yang direstui semesta untuk ditakdirkan menua bersama.*_",
    "_*aku hanya kehilangan orang yang tidak mencintaiku, tapi kamu kehilangan seseorang yang benar benar tulus padamu*_",
    "_*aku terlalu menyukaimu dan berharap padamu, sampai sampai aku menceritakan tentang dirimu kepada teman teman ku seolah olah kamu sudah menjadi milikku.*_",
    "_*terimakasih telah memberikan banyak pelajaran tentang hidup. salah satunya 'mendewasakan diri'. dengan cara mengikhlaskan sesuatu yang bukan milik dan menerimanya dengan lapang dada tanpa harus menghakimi dan membenci siapapun sumbernya.*_",
    "_*dodo ganteng kata mama dan teman2*_",
    "_*dia tidak tahu yang sebenarnya, bahwa saya ingin mencintainya dengan sangat hebat. ketika saya menjauh darinya itu tidak berarti saya tidak suka. tetapi saya menghindarinya karena saya sadar bahwa saat ini, banyak hal yang memungkinkan kita untuk terjebak dalam situasi yang salah.*_",
    "_*jangan pernah meletakkan kebahagiaan dirimu sepenuhnya diatas kehidupan seseorang ketika sedang jatuh cinta, karena pada akhirnya kita akan merasa kehilangan entah karena luka dari salah satu pihak atau kematian. dan yang tersisa, kekuatan cinta akan kebahagiaan di atas diri sendirilah yang menguatkan.*_",
    "_*berusaha untuk memandang orang dengan isi positif, tidak membuatmu dipandang begitu pula. its okay, self control is the chief element in self respect !*_",
    "_*semua kesedihan dan masalah yang kamu hadapi saat ini mengarahkan kamu ke arah yang baik, dan rasa sakit yang kamu rasakan hari ini akan mendewasakan kamu jadi semua ada tujuan tersendiri dari Tuhan untuk kamu.*_",
    "_*semesta pasti punya tujuan, ya walaupun tidak menyenangkan setidaknya mendewasakan.*_",
    "_*i love you. only you. i'm not going to get bored of you, i'm not going to lose feelings for you. i'm not going to hurt you. i want you and only you.*_",
    "_*lupakan aku ku sayangi mu tak berarti bahwa ku bisa memilikimu maaf kan ak tidak bisa memberi yang terbaik tapi jika kau membutuh kan ku untuk mendampingimu di saat hari-hari buruk mu aku kan selalu sedia berada di sisi mu.*_",
)


def odo(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = (
        message.reply_to_message.reply_photo
        if message.reply_to_message
        else message.reply_photo
    )
    reply_photo(random.choice(hachi_strings.HACHI_IMG))


def ipe(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = (
        message.reply_to_message.reply_photo
        if message.reply_to_message
        else message.reply_photo
    )
    reply_photo(random.choice(JJ_STRING))


LAWAK_STRINGS = (
    "https://telegra.ph/file/abdae436beade5626f568.mp4",
    "https://telegra.ph/file/776897d2aa2de78cd59c7.mp4",
    "https://telegra.ph/file/266d16b4d941b3953a3ea.mp4",
    "https://telegra.ph/file/fab2d5b2e871b26febe8c.mp4",
    "https://telegra.ph/file/697428078668a59f06739.mp4",
    "https://telegra.ph/file/e1558f2984f90048017ff.mp4",
    "https://telegra.ph/file/036333fb4ce099b7ca02a.mp4",
    "https://telegra.ph/file/68bc77491d66c0327871b.mp4",
    "https://telegra.ph/file/22b9ce3a337eb8e33d1c0.mp4",
    "https://telegra.ph/file/c90c054916841dc1e684b.mp4",
    "https://telegra.ph/file/fc9c27ecb8355335238ca.mp4",
    "https://telegra.ph/file/27b4aa97616c7c8635138.mp4",
    "https://telegra.ph/file/7258217e42a7bf599393f.jpg",
    "https://telegra.ph/file/a2e5fdbf9aa470941a802.mp4",
    "https://telegra.ph/file/edcfff121ce671c6be6cb.mp4",
    "https://telegra.ph/file/d22b6c185db8f4a3014fa.mp4",
    "https://telegra.ph/file/31075c5d489fea8868f83.mp4",
    "https://telegra.ph/file/fc542bfd2dd7531217954.mp4",
    "https://telegra.ph/file/fe7a210c8a342dcdc5859.mp4",
    "https://telegra.ph/file/1dbe21330117db62b61fc.mp4",
    "https://telegra.ph/file/58a4e245bbc2b35492024.mp4",
    "https://telegra.ph/file/48b3daa3a20559d900129.mp4",
    "https://telegra.ph/file/64027fb4b791a27f6b5cb.mp4",
    "https://telegra.ph/file/620140f79810d23641fc6.mp4",
    "https://telegra.ph/file/7bfb94c861f82c18cb433.mp4",
    "https://telegra.ph/file/923ac2158b93ba9fc17dd.mp4",
    "https://telegra.ph/file/3048d569911fe1cdd187b.mp4",
    "https://telegra.ph/file/c7c5c80ce21909f75580b.mp4",
    "https://telegra.ph/file/9c138d8201462b1f81447.mp4",
    "https://telegra.ph/file/018625bf11eb48adb810e.mp4",
    "https://telegra.ph/file/97f2b6789d706ae4ea030.mp4",
    "https://telegra.ph/file/6a5e42335998ea38f9e22.mp4",
    "https://telegra.ph/file/e957da8844f7b26549b0c.mp4",
    "https://telegra.ph/file/e145546bb0bc2fbeec647.mp4",
    "https://telegra.ph/file/432963b28bd1a1436c36d.mp4",
    "https://telegra.ph/file/21e4e12a83ce00b937e33.mp4",
    "https://telegra.ph/file/af0d778e512f98d769d3b.mp4",
)


JJ_STRING = (
    "https://telegra.ph/file/e188e5744b039cc30dca2.jpg",
    "https://telegra.ph/file/5088c032502d6bac26a57.jpg",
    "https://telegra.ph/file/2035a4c23545acc82a6dc.jpg",
    "https://telegra.ph/file/70369c2d06ff2879b6569.jpg",
    "https://telegra.ph/file/d017e355464bea37efe33.jpg",
    "https://telegra.ph/file/f8b5376041a2c34228183.jpg",
    "https://telegra.ph/file/e5a6416a77e7d5f79ce36.jpg",
    "https://telegra.ph/file/aec00301c8f709f658bd6.jpg",
    "https://telegra.ph/file/30e6fa693fe2a78031dc2.jpg",
    "https://telegra.ph/file/894bd6c7abbfaf042231f.jpg",
    "https://telegra.ph/file/174e776e0d2537f182930.jpg",
    "https://telegra.ph/file/ffc89336bc9adb4c0ecaa.jpg",
    "https://telegra.ph/file/2faca8b6f12d37bb7344a.jpg",
    "https://telegra.ph/file/31e7802afefa2e685102e.jpg",
)


def lawak(update, context):
    msg = update.effective_message
    msg.reply_video(
        random.choice(LAWAK_STRINGS),
        caption=f"""<i>Powered by: Hachi Robot</i> 🔥""",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support", url="https://t.me/demonszxx"),
                ],
            ]
        ),
    )


def diaryadodo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(random.choice(AD_STRINGS), parse_mode=ParseMode.MARKDOWN)


__help__ = """
 ❍ `/odo`*:* gives random demons media.
 ❍ `/ipe`*:* gives random poto nya ipe
 ❍ `/asupan`*:* gives random asupan medi.
 ❍ `/chika`*:* gives random chika media.
 ❍ `/wibu`*:* gives random wibu media.
 ❍ `/lawak`*:* gives random lawak media.
 ❍ `/apakah`*:* For ask question about someone with AI.
 ❍ `/diarydodo`*:* Check Aja.
 ❍ `/apod`*:* Get Astronomy Picture of Day by NASA.
 ❍ `/devian` <search query> ; <no of pics> *:* Devian-Art Image Search.
 ❍ `/joke`*:* To get random joke.
 ❍ `/inslut`*:* Insult someone.
 ❍ `/bugil`*:*nbuat yang sangean kek mas almin.
 ❍ `/url <long url>`*:* To get a shorten link of long link.
 ❍ `/carbon` <text> [or reply] *:* Beautify your code using carbon.now.sh
 ❍ `/phone <number>`*:* To get info about that number
 ❍ `/webss` <url> *:* Take A Screenshot Of A Webpage.
"""


ODO_HANDLER = DisableAbleCommandHandler("odo", odo, run_async=True)
dispatcher.add_handler(ODO_HANDLER)
IPE_HANDLER = DisableAbleCommandHandler("ipe", ipe, run_async=True)
dispatcher.add_handler(IPE_HANDLER)
LAWAK_HANDLER = DisableAbleCommandHandler("lawak", lawak, run_async=True)
dispatcher.add_handler(LAWAK_HANDLER)
DIARYDODO_HANDLER = DisableAbleCommandHandler("diarydodo", diaryadodo, run_async=True)
dispatcher.add_handler(DIARYDODO_HANDLER)

__mod_name__ = "Hachi Extras"


__command_list__ = ["odo", "ipe", "diarydodo", "lawak"]
__handlers__ = [ODO_HANDLER, IPE_HANDLER, DIARYDODO_HANDLER, LAWAK_HANDLER]
