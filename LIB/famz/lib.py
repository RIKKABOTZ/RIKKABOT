#example
#prefix = '#'
#blocked = []   
#limitawal = '10' 
#memberlimit = 0
#//function
#const getLevelingXp = (sender) => {
            let position = false
            Object.keys(_level).forEach((i) => {
                if (_level[i].id === sender) {
                    position = i
                }
         
#})
            if (position !== false) {
                return _level[position].xp
            }
        }

#const getLevelingLevel = (sender) => {
            let position = false
            Object.keys(_level).forEach((i) => {
                if (_level[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                return _level[position].level
            }
        }
#const getLevelingId = (sender) => {
            let position = false
            Object.keys(_level).forEach((i) => {
                if (_level[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                return _level[position].id
            }
        }
#const addLevelingXp = (sender, amount) => {
            let position = false
            Object.keys(_level).forEach((i) => {
                if (_level[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                _level[position].xp += amount
                fs.writeFileSync('./database/user/level.json', JSON.stringify(_level))
            }
        }
#const addLevelingLevel = (sender, amount) => {
            let position = false
            Object.keys(_level).forEach((i) => {
                if (_level[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                _level[position].level += amount
                fs.writeFileSync('./database/user/level.json', JSON.stringify(_level))
            }
        }
#const addLevelingId = (sender) => {
            const obj = {id: sender, xp: 1, level: 1}
            _level.push(obj)
            fs.writeFileSync('./database/user/level.json', JSON.stringify(_level))
        }
        
#const getLimit = (sender) => {
        	let position = false
              Object.keys(limit).forEach ((i) => {
              	if (limit[position].id === sender) {
              	   position = i
                  }
              })
             if (position !== false) {
                return limit[position].limit
            }
        }
#const getLimit = (sender) => {
        	let position = false
              Object.keys(limit).forEach ((i) => {
              	if (limit[position].id === sender) {
              	   position = i
                  }
              })
             if (position !== false) {
                return limit[position].limit
            }
        }
#const addRegisteredUser = (userid, sender, age, time, serials) => {
            const obj = { id: userid, name: sender, age: age, time: time, serial: serials }
            _registered.push(obj)
            fs.writeFileSync('./database/bot/registered.json', JSON.stringify(_registered))
        }
#const createSerial = (size) => {
            return crypto.randomBytes(size).toString('hex').slice(0, size)
        }
#const checkRegisteredUser = (sender) => {
            let status = false
            Object.keys(_registered).forEach((i) => {
                if (_registered[i].id === sender) {
                    status = true
                }
            })
            return status
        }
        
        const addATM = (sender) => {
        	const obj = {id: sender, uang : 0}
            uang.push(obj)
            fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
        }
        
#const addKoinUser = (sender, amount) => {
            let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                uang[position].uang += amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
#
#const checkATMuser = (sender) => {
        	let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                return uang[position].uang
            }
        }

#const bayarLimit = (sender, amount) => {
        	let position = false
            Object.keys(_limit).forEach((i) => {
                if (_limit[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                _limit[position].limit -= amount
                fs.writeFileSync('./database/user/limit.json', JSON.stringify(_limit))
            }
        }
#
#const confirmATM = (sender, amount) => {
        	let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                uang[position].uang -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
#const limitAdd = (sender) => {
             let position = false
            Object.keys(_limit).forEach((i) => {
                if (_limit[i].id == sender) {
                    position = i
                }
            })
            if (position !== false) {
                _limit[position].limit += 1
                fs.writeFileSync('./database/user/limit.json', JSON.stringify(_limit))
            }
        }
#RIKKA.on('group-participants-update', async (anu) => {
		if (!welkom.includes(anu.jid)) return
		try {
			const mdata = await akira.groupMetadata(anu.jid)
			console.log(anu)
			if (anu.action == 'add') {
				num = anu.participants[0]
					pp_user = 'https://i.ibb.co/B6mZsR9/20210403-182628.jpg'
				teks = `
ʜᴀʟʟᴏ
@${num.split('@')[0]}
👋\nꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ɢʀᴏᴜᴘ 
*${mdata.subject}*
┏━━━━━━━━━━━━━━━
┃────「 *_ɪɴᴛʀᴏ_* 」─────
┃━━━━━━━━━━━━━━━
┠⊷️ *ɴᴀᴍᴀ* :
┠⊷️ *ᴜᴍᴜʀ* :
┠⊷️ *ɴᴀᴍᴀ ᴘᴀᴄᴀʀ* :
┠⊷️ *ʜᴏʙʙʏ* :
┠⊷️ *ɢᴇɴᴅᴇʀ* :
┠⊷️ *ᴀꜱᴀʟ ᴋᴏᴛᴀ* :
┗━━━━━━━━━━━━━━━`
				
#let buff = await getBuffer(pp_user)
				akira.sendMessage(mdata.id, buff, MessageType.image, {caption: teks, contextInfo: {"mentionedJid": [num]}})
			} else if (anu.action == 'remove') {
				num = anu.participants[0]
					pp_user = 'https://i.ibb.co/ZSV8q3y/20210403-183459.jpg'
				teks = `
sᴇʟᴀᴍᴀᴛ ᴛɪɴɢɢᴀʟ 
@${num.split('@')[0]}👋🍻
sᴇᴍᴏɢᴀ ᴊᴀsᴀᴅᴍᴜ ʙᴀɪᴋ ʙᴀɪᴋ sᴀᴊᴀ ᴅᴀɴ sᴇʟᴀʟᴜ ᴅɪᴋᴇɴᴀɴɢ ᴏʟᴇʜ ᴏʀᴀɴɢ ʏɢ ʙᴇʀᴀᴅᴀ ᴅɪsɪɴɪ🚮`
				let buff = await getBuffer(pp_user)
				RIKKA.sendMessage(mdata.id, buff, MessageType.image, {caption: teks, contextInfo: {"mentionedJid": [num]}})
			}
		} catch (e) {
			console.log('Error : %s', color(e, 'red'))
		}
	})
	
#const isLimit = (sender) =>{ 
		      let position = false
              for (let i of _limit) {
              if (i.id === sender) {
              	let limits = i.limit
              if (limits >= limitawal ) {
              	  position = true
                    akira.sendMessage(from, ind.limitend(pushname), text, {quoted: mek})
                    return true
              } else {
              	_limit
                  position = true
                  return false
               }
             }
           }
           if (position === false) {
           	const obj = { id: sender, limit: 1 }
                _limit.push(obj)
                fs.writeFileSync('./database/user/limit.json',JSON.stringify(_limit))
           return false
       }
     }
#             if (mesejAnti.includes("://chat.whatsapp.com/")){
		        if (!isGroup) return
		        if (!isAntiLink) return
		        if (isGroupAdmins) return reply('Admin Grup Mah Bebas:D')
		        akira.updatePresence(from, Presence.composing)
		        if (mesejAnti.includes(",izinkak")) return reply("Iya kak jangan spam ya")
		        var kic = `${sender.split("@")[0]}@s.whatsapp.net`
		        reply(`Maaf kak ${sender.split("@")[0]} Grup ini anti link, siap siap kamu di kick`)
		        setTimeout( () => {
			        akira.groupRemove(from, [kic]).catch((e)=>{reply(`*${namabot} HARUS JADI ADMINâ—*`)})
		        }, 3000)
		        setTimeout( () => {
			        akira.updatePresence(from, Presence.composing)
			        reply("ShenraTensei🌪️")
		        }, 2000)
		        setTimeout( () => {
			        akira.updatePresence(from, Presence.composing)
			        reply("Isi Cakraa☁️")
		        }, 1000)
		        setTimeout( () => {
			        akira.updatePresence(from, Presence.composing)
			        reply("Ready?...")
		        }, 0)
		  }
		  
#case 'menu':
                 if (!isRegistered) return reply( ind.noregis())
				if (isBanned) return reply(ind.baned())
					const reqXp  = 5000 * (Math.pow(2, getLevelingLevel(sender)) - 1)
					const uangku = checkATMuser(sender)
                    wew = fs.readFileSync(`./akiraganz/logo.jpg`)
                    databaseuhy = `
╭══─⊱ ❰ *_User ${namabot}_* ❱ ⊰─═
├➤ ɴᴀᴍᴀ : ${pushname}
├➤ ɴᴏᴍᴏʀ : wa.me/${sender.split("@")[0]}
├➤ ᴜᴀɴɢ : Rp${uangku}
├➤ xᴘ : ${getLevelingXp(sender)}/${reqXp}
├➤ ʟᴇᴠᴇʟ : ${getLevelingLevel(sender)}
├➤ ᴜsᴇʀ ʀᴇɢɪsᴛᴇʀ : ${_registered.length}
╰──── ⸨ *_${namabot}_* ⸩ ⊰─═══

◪ ɪɴғᴏ ᴀᴋɪʀᴀ
❏ *ɴᴀᴍᴀ:* 
RIKKA ( Pras) 
  ----------------------------------
╔═════════════════❍
║⸨𝐑𝐮𝐥𝐞𝐬 - 𝐒𝐢𝐦𝐩𝐥𝒆⸩
║▬▭▬▭▬▭▬▭▬▭
║⧐ ⸨ *sᴘᴀᴍ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ!* ⸩
║⧐ ⸨ *ʙᴇʀɪ ᴊᴇᴅᴀ 6 ᴅᴇᴛɪᴋ!* ⸩
║⧐ ⸨ *ᴇʀʀᴏʀ ʜᴜʙᴜɴɢɪ ᴏᴡɴᴇʀ!* ⸩
║⧐ ⸨ *ᴊᴀɴɢᴀɴ ʙᴀɴᴅɪɴɢᴋᴀɴ ʙᴏᴛ* ⸩
║⧐ ⸨ *ᴋᴇᴛɪᴋ ${prefix}ʜᴇʟᴘ* ⸩
║⧐ ⸨ *ᴊᴀɴɢᴀɴ ᴠᴄ/ᴄᴀʟʟ!* ⸩
║⧐ ⸨ *ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʀᴀᴍᴀʜ* ⸩
║▬▭▬▭▬▭▬▭▬▭
╚═════════════════❍
╔═════════════════❍
║⸨*ɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ᴅᴇɴɢᴀɴ ʙᴀɪᴋ!*⸩
║▬▭▬▭▬▭▬▭▬▭
║⧐ ⸨ *ᴘʀᴇғɪx sᴀᴀᴛ ɪɴɪ ${prefix}* ⸩
║⧐ ⸨ *ᴋᴇᴛɪᴋ ${prefix}rules* ⸩
║⧐ ⸨ *кᴇᴛɪᴋ ${prefix}info* ⸩
║▬▭▬▭▬▭▬▭▬▭
╠═════════════════❍
║⧐ ɪɴɢɪɴ sᴇᴡᴀ ʙᴏᴛ? *${prefix}sewabot*
╠═════════════════════
║      ╔╦╦╦═╦╗╔═╦═╦══╦═╗
║      ║║║║╩╣╚╣═╣║║║║║╩╣
║      ╚══╩═╩═╩═╩═╩╩╩╩═╝
╠═══════════════════❍
╠═════════════════════
║> *_Menu ${namabot}_*
╠═════════════════════
║┏━━⊱*「 𝗢𝗧𝗛𝗘𝗥 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}info*
║┣❏ *${prefix}rules*
║┣❏ *${prefix}owner*
║┣❏ *${prefix}sewabot*
║┣❏ *${prefix}setnamabot*
║┣❏ *${prefix}daftar*
║┣❏ *${prefix}cekapikey*
║┃
║┣━━⊱*「𝗔𝗡𝗧𝗜 𝗩𝗜𝗥𝗧𝗘𝗫 𝗠𝗘𝗡𝗨」* 
║┃
║┣❏ *${prefix}antivirtex*
║┣❏ *${prefix}antialakazam*
║┣❏ *${prefix}antixvirus*
║┣❏ *${prefix}antivirustebel*
║┣❏ *${prefix}anticollosal*
║┣❏ *${prefix}antiviruschina*
║┃
║┣━━⊱*「 𝗡𝗘𝗪 𝗙𝗜𝗧𝗨𝗥𝗘 」* 
║┃
║┣❏ *${prefix}skeleton*
║┣❏ *${prefix}avatarhacker*
║┣❏ *${prefix}watermaker*
║┣❏ *${prefix}ballon*
║┣❏ *${prefix}girlgrafity*
║┣❏ *${prefix}matrick*
║┣❏ *${prefix}viettel*
║┣❏ *${prefix}glowmetallic*
║┣❏ *${prefix}textgoogle*
║┣❏ *${prefix}tinyurl*
║┣❏ *${prefix}githubstalk*
║┣❏ *${prefix}ytstalk*
║┣❏ *${prefix}tkstalk*
║┣❏ *${prefix}attp2*
║┣❏ *${prefix}tebakbendera*
║┣❏ *${prefix}hilih*
║┣❏ *${prefix}alay*
║┣❏ *${prefix}nulis4*
║┣❏ *${prefix}nulis5*
║┣❏ *${prefix}amongus*
║┣❏ *${prefix}namaninja*
║┣❏ *${prefix}tebakumur*
║┣❏ *${prefix}besarkecil*
║┣❏ *${prefix}ytkomen*
║┣❏ *${prefix}phkomen*
║┣❏ *${prefix}jodoh*
║┣❏ *${prefix}jadian*
║┣❏ *${prefix}weton*
║┣❏ *${prefix}tebakumur*
║┣❏ *${prefix}purba*
║┣❏ *${prefix}cekapikey*
║┃
║┣━━⊱*「 𝗦𝗘𝗔𝗥𝗖𝗛 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}shopee*
║┣❏ *${prefix}google*
║┣❏ *${prefix}gimage*
║┣❏ *${prefix}gimage2*
║┣❏ *${prefix}konachan*
║┣❏ *${prefix}playstore*
║┣❏ *${prefix}stickerwa*
║┣❏ *${prefix}wallpapersearch*
║┣❏ *${prefix}wallpapersearch2*
║┣❏ *${prefix}ytsearch*
║┣❏ *${prefix}wikipedia*
║┣❏ *${prefix}translate*
║┃
║┣━━⊱*「 𝗔𝗦𝗨𝗣𝗔𝗡 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}asupan*
║┣❏ *${prefix}asupan2*
║┣❏ *${prefix}asupanrana*
║┣❏ *${prefix}asupanamel*
║┣❏ *${prefix}asupankaia*
║┣❏ *${prefix}asupanuna*
║┃
║┣━━⊱*「 ??𝗔𝗞𝗘𝗥 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}sticker* 
║┣❏ *${prefix}︎shadow*
║┣❏ *${prefix}cup*
║┣❏ *${prefix}cup1*
║┣❏ *${prefix}googlesearch*
║┣❏ *${prefix}avenger*
║┣❏ *${prefix}smoke*
║┣❏ *${prefix}burnpaper*
║┣❏ *${prefix}lovemessage*
║┣❏ *${prefix}undergrass*
║┣❏ *${prefix}valorantbanner*
║┣❏ *${prefix}fflogo*
║┣❏ *${prefix}newyearcard*
║┣❏ *${prefix}bannerlol*
║┣❏ *${prefix}captainamerica*
║┣❏ *${prefix}itxt*
║┣❏ *${prefix}starnight*
║┣❏ *${prefix}codbanner*
║┣❏ *${prefix}love*
║┣❏ *${prefix}woodheart*
║┣❏ *${prefix}flowerheart*
║┣❏ *${prefix}woodenboard*
║┣❏ *${prefix}darkneon*
║┣❏ *${prefix}candlemug*
║┣❏ *${prefix}lovemsg*
║┣❏ *${prefix}mugflower*
║┣❏ *${prefix}narutobanner*
║┣❏ *${prefix}paperonglass*
║┣❏ *${prefix}romancetext*
║┣❏ *${prefix}shadowtext*
║┣❏ *${prefix}qrcode*
║┣❏ *${prefix}emojitopng*
║┣❏ *${prefix}glowingneon*
║┣❏ *${prefix}space*
║┣❏ *${prefix}hpotter*
║┣❏ *${prefix}woodblock*
║┣❏ *${prefix}summer3d*
║┣❏ *${prefix}hartatahta*
║┣❏ *${prefix}wolfmetal*
║┣❏ *${prefix}nature3d*
║┣❏ *${prefix}underwater*
║┣❏ *${prefix}golderrose*
║┣❏ *${prefix}lionlogo*
║┣❏ *${prefix}ninjalogo*
║┣❏ *${prefix}marvelstudio*
║┣❏ *${prefix}wolflogo*
║┣❏ *${prefix}steel3d*
║┣❏ *${prefix}wallgravity*
║┣❏ *${prefix}summernature*
║┣❏ *${prefix}letterleaves*
║┣❏ *${prefix}fallleaves*
║┣❏ *${prefix}flamming*
║┣❏ *${prefix}harrypotter*
║┣❏ *${prefix}futureneon*
║┣❏ *${prefix}breakwall*
║┣❏ *${prefix}carvedwood*
║┣❏ *${prefix}wetglass*
║┣❏ *${prefix}multicolor3d*
║┣❏ *${prefix}watercolor*
║┣❏ *${prefix}luxurygold*
║┣❏ *${prefix}galaxywallpaper*
║┣❏ *${prefix}lighttext*
║┣❏ *${prefix}beautifulflower*
║┣❏ *${prefix}puppycute*
║┣❏ *${prefix}royaltext*
║┣❏ *${prefix}heartshaped*
║┣❏ *${prefix}birthdaycake*
║┣❏ *${prefix}galaxystyle
║┣❏ *${prefix}hologram3d*
║┣❏ *${prefix}glossychrome*
║┣❏ *${prefix}greenbush*
║┣❏ *${prefix}metallogo*
║┣❏ *${prefix}noeltext*
║┣❏ *${prefix}glittergold*
║┣❏ *${prefix}textcake*
║┣❏ *${prefix}starsnight*
║┣❏ *${prefix}wooden3d*
║┣❏ *${prefix}textbyname*
║┣❏ *${prefix}writegalacy*
║┣❏ *${prefix}galaxybat*
║┣❏ *${prefix}snow3d*
║┣❏ *${prefix}birthdayday*
║┣❏ *${prefix}freefire*
║┣❏ *${prefix}textdaun*
║┣❏ *${prefix}nulis*
║┣❏ *${prefix}silktext*
║┣❏ *${prefix}makequote*
║┣❏ *${prefix}toimg*
║┣❏ *${prefix}ocr*
║┣❏ *${prefix}galaxstyle*
║┣❏ *${prefix}jokerlogo*
║┣❏ *${prefix}toxic*
║┣❏ *${prefix}bloodfrosted*
║┣❏ *${prefix}hororblood*
║┣❏ *${prefix}halloween*
║┣❏ *${prefix}pemainbola*
║┣❏ *${prefix}firework*
║┣❏ *${prefix}glitch*
║┣❏ *${prefix}blackpink*
║┣❏ *${prefix}goldplay*
║┣❏ *${prefix}hologram*
║┣❏ *${prefix}textbyname*
║┣❏ *${prefix}herrypoter*
║┣❏ *${prefix}metallogo*
║┣❏ *${prefix}ttp*
║┣❏ *${prefix}thunder*
║┣❏ *${prefix}bokeh*
║┣❏ *${prefix}strawberry*
║┣❏ *${prefix}metaldark*
║┣❏ *${prefix}textdaun*
║┣❏ *${prefix}nulis*
║┣❏ *${prefix}silktext*
║┣❏ *${prefix}quotesmaker*
║┣❏ *${prefix}quotesmaker2*
║┣❏ *${prefix}emojitosticker*
║┣❏ *${prefix}toimg*
║┣❏ *${prefix}ocr*
║┣❏ *${prefix}galaxstyle*
║┣❏ *${prefix}jokerlogo*
║┣❏ *${prefix}triggered*
║┣❏ *${prefix}gtav*
║┣❏ *${prefix}gay*
║┣❏ *${prefix}nigthbeach*
║┣❏ *${prefix}laptop*
║┣❏ *${prefix}linephoto*
║┣❏ *${prefix}raindrop*
║┣❏ *${prefix}sketch*
║┣❏ *${prefix}wanted*
║┣❏ *${prefix}crossgun*
║┣❏ *${prefix}bloodfrosted*
║┣❏ *${prefix}hororblood*
║┣❏ *${prefix}gamelogo*
║┣❏ *${prefix}halloween*
║┣❏ *${prefix}firework*
║┣❏ *${prefix}goldplay*
║┣❏ *${prefix}silverplaybutton*
║┣❏ *${prefix}hologram*
║┣❏ *${prefix}textbyname*
║┣❏ *${prefix}herrypoter*
║┣❏ *${prefix}imagetext*
║┣❏ *${prefix}greenneon*
║┣❏ *${prefix}metallogo* 
║┃
║┣━━⊱*「 𝗜𝗠𝗔𝗚𝗘 𝗘𝗗𝗜𝗧 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏  *${prefix}wanted*
║┣❏  *${prefix}gtav*
║┣❏  *${prefix}facebookpage*
║┣❏  *${prefix}costumwp*
║┣❏  *${prefix}pantaimalam*
║┣❏  *${prefix}pencil*
║┣❏  *${prefix}bakar*
║┣❏  *${prefix}crossgun*
║┣❏  *${prefix}hitler*
║┣❏  *${prefix}trash*
║┣❏  *${prefix}picture*
║┣❏  *${prefix}blur*
║┣❏  *${prefix}invert*
║┣❏  *${prefix}meme atas/bawah*
║┃
║┣━━⊱*「 𝗦𝗘𝗥𝗧𝗜𝗙𝗜𝗞𝗔𝗧 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏  *${prefix}*anakharamserti*
║┣❏  *${prefix}*hekelserti* 
║┣❏  *${prefix}*babuserti* 
║┣❏  *${prefix}*ffserti* 
║┣❏  *${prefix}*bucinserti* 
║┣❏  *${prefix}*bocilepepserti* 
║┣❏  *${prefix}*gayserti* 
║┣❏  *${prefix}*pacarserti* 
║┣❏  *${prefix}*sadboyserti* 
║┣❏  *${prefix}*surgaserti* 
║┣❏  *${prefix}*pinterserti*
║┣❏  *${prefix}*badgirlserti*
║┣❏  *${prefix}*badboyserti*
║┣❏  *${prefix}*goodgirlserti*
║┣❏  *${prefix}*goodboyserti*
║┣❏  *${prefix}*editodberkelasserti*
║┣❏  *${prefix}*goodlookingserti*
║┣❏  *${prefix}*fucekboyserti*
║┣❏  *${prefix}*jametserti*
║┣❏  *${prefix}*youtuberserti*
║┣❏  *${prefix}*fftourserti*
║┣❏  *${prefix}*fftourserti2*
║┣❏  *${prefix}*fftourserti3*
║┣❏  *${prefix}*fftourserti4*
║┣❏  *${prefix}*fftourserti5*
║┣❏  *${prefix}*mltourserti*
║┣❏  *${prefix}*mltourserti2*
║┣❏  *${prefix}*mltourserti3*
║┣❏  *${prefix}*mltourserti4*
║┣❏  *${prefix}*mltourserti5*
║┣❏  *${prefix}*pubgtourserti*
║┣❏  *${prefix}*pubgtourserti2*
║┣❏  *${prefix}*pubgtourserti3*
║┣❏  *${prefix}*pubgtourserti4*
║┣❏  *${prefix}*pubgtourserti5*
║┃
║┣━━⊱*「 𝗦𝗧𝗜𝗖𝗞𝗘𝗥 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏  *${prefix}sticker*
║┣❏  *${prefix}stickerwm* 
║┣❏  *${prefix}ttp* 
║┣❏  *${prefix}ttp2* 
║┣❏  *${prefix}ttp3*
║┣❏  *${prefix}ttp4* 
║┣❏  *${prefix}attp* 
║┣❏  *${prefix}toimg* 
║┣❏  *${prefix}ngif* 
║┣❏  *${prefix}nsfwnekogif* 
║┣❏  *${prefix}randomhentaigif* 
║┣❏  *${prefix}semoji* 
║┣❏  *${prefix}stickerwa* 
║┣❏  *${prefix}triggered* 
║┣❏  *${prefix}stickerspongebob* 
║┣❏  *${prefix}stickerpatrick* 
║┣❏  *${prefix}stickersearch*  
║┣❏  *${prefix}telesticker*
║┃
║┣━━⊱*「 𝗟𝗜𝗡𝗞 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}bitly*
║┣❏ *${prefix}cuttly*
║┣❏ *${prefix}tinyurl*
║┣❏ *${prefix}shortlink*
║┣❏ *${prefix}shortlink2*
║┣❏ *${prefix}shortlink3*
║┣❏ *${prefix}shortlink4*
║┣❏ *${prefix}shortlink5*
║┣❏ *${prefix}shortlink6*
║┃
║┣━━⊱*「 𝗙𝗨𝗡 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}beban*
║┣❏ *${prefix}cantik*
║┣❏ *${prefix}audio*
║┣❏ *${prefix}mining*
║┣❏ *${prefix}playstore*
║┣❏ *${prefix}slap*
║┣❏ *${prefix}tampar*
║┣❏ *${prefix}bisakah*
║┣❏ *${prefix}kapankah*
║┣❏ *${prefix}apakah*
║┣❏ *${prefix}seberapagay*
║┣❏ *${prefix}rate*
║┣❏ *${prefix}truth*
║┣❏ *${prefix}dare*
║┣❏ *${prefix}hobby*
║┣❏ *${prefix}beban*
║┣❏ *${prefix}ganteng*
║┣❏ *${prefix}cantik*
║┣❏ *${prefix}memeindo*
║┣❏ *${prefix}darkjoke*
║┣❏ *${prefix}cerpen*
║┣❏ *${prefix}quotesimage*
║┣❏ *${prefix}fitnah*
║┣❏ *${prefix}pasangan*
║┣❏ *${prefix}ntahlah*
║┣❏ *${prefix}slap*
║┣❏ *${prefix}quotesmotivasi*
║┣❏ *${prefix}quotessehat*
║┣❏ *${prefix}quotescinta*
║┣❏ *${prefix}hemkel*
║┣❏ *${prefix}quotes2*
║┣❏ *${prefix}katadoi*
║┣❏ *${prefix}katakatadilan*
║┣❏ *${prefix}qoutes*
║┣❏ *${prefix}caklontong*
║┣❏ *${prefix}family100*
║┣❏ *${prefix}tebakgambar*
║┣❏ *${prefix}kbbi*
║┣❏ *${prefix}dadu*
║┣❏ *${prefix}artinama*
║┃
║┣━━⊱*「 𝗦𝗜𝗠𝗣𝗟𝗘 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}nulis*
║┣❏ *${prefix}nulis2*
║┣❏ *${prefix}nulis3*
║┣❏ *${prefix}nulis4*
║┣❏ *${prefix}semoji* 
║┣❏ *${prefix}fakedonald*
║┣❏ *${prefix}ktpmaker*
║┣❏ *${prefix}wame*
║┣❏ *${prefix}joox*
║┣❏ *${prefix}stalkig*
║┣❏ *${prefix}tiktokstalk*
║┣❏ *${prefix}ytsearch*
║┣❏ *${prefix}ytmp3*
║┣❏ *${prefix}ytmp4*
║┣❏ *${prefix}play*
║┣❏ *${prefix}ssweb*
║┣❏ *${prefix}googlesearch*
║┣❏ *${prefix}ytsearch*
║┃
║┣━━⊱*「 𝗔𝗡𝗜𝗠𝗘 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}character*
║┣❏ *${prefix}manga*
║┣❏ *${prefix}animesaran*
║┣❏ *${prefix}animesaran2*
║┣❏ *${prefix}husbu2*
║┣❏ *${prefix}anime*
║┣❏ *${prefix}wallpaperanime*
║┣❏ *${prefix}trap*
║┣❏ *${prefix}baka2*
║┣❏ *${prefix}wallpapernime*
║┣❏ *${prefix}animefanart*
║┣❏ *${prefix}megumin*
║┣❏ *${prefix}shinobu*
║┣❏ *${prefix}baka*
║┣❏ *${prefix}eroyuri*
║┣❏ *${prefix}happy*
║┣❏ *${prefix}dance*
║┣❏ *${prefix}neko3*
║┣❏ *${prefix}smile*
║┣❏ *${prefix}wallpaper*
║┣❏ *${prefix}slapnime*
║┣❏ *${prefix}shota*
║┣❏ *${prefix}sagiri*
║┣❏ *${prefix}femdom*
║┣❏ *${prefix}waifukawai*
║┣❏ *${prefix}kuni*
║┣❏ *${prefix}kitsune*
║┣❏ *${prefix}yuri*
║┣❏ *${prefix}yaoi*
║┣❏ *${prefix}wancak*
║┣❏ *${prefix}quotesnime*
║┣❏ *${prefix}waifu2*
║┣❏ *${prefix}bj*
║┣❏ *${prefix}ram*
║┣❏ *${prefix}pictlolicon*
║┣❏ *${prefix}pictneko*
║┣❏ *${prefix}testwaifu*
║┣❏ *${prefix}nsfw_avatar*
║┣❏ *${prefix}senku*
║┣❏ *${prefix}pictwaifu*
║┣❏ *${prefix}kurumi2*
║┣❏ *${prefix}nakanomiku*
║┣❏ *${prefix}waifu2*
║┣❏ *${prefix}waifu*
║┣❏ *${prefix}loli*
║┣❏ *${prefix}loli2*
║┣❏ *${prefix}neko*
║┣❏ *${prefix}neko2*
║┣❏ *${prefix}nekonime*
║┣❏ *${prefix}randomanime*
║┣❏ *${prefix}randomhusbu*
║┣❏ *${prefix}wibu*
║┣❏ *${prefix}wibu2*
║┣❏ *${prefix}boruto*
║┣❏ *${prefix}rize*
║┣❏ *${prefix}kaneki*
║┣❏ *${prefix}kemonomimi*
║┣❏ *${prefix}holo*
║┣❏ *${prefix}naruto*
║┣❏ *${prefix}amv*
║┣❏ *${prefix}minato*                                                                               ║┣❏ *${prefix}tagall*
║┣❏ *${prefix}gecg*
║┣❏ *${prefix}avatar*
║┣❏ *${prefix}miku*
║┣❏ *${prefix}kurumi*
║┣❏ *${prefix}hinata*
║┣❏ *${prefix}sasuke*
║┣❏ *${prefix}sakura*
║┣❏ *${prefix}akura*
║┣❏ *${prefix}itori*
║┣❏ *${prefix}touka*
║┣❏ *${prefix}rem*
║┣❏ *${prefix}chika*
║┃
║┣━━⊱*「 𝗜𝗦𝗟𝗔𝗠 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}quran*
║┣❏ *${prefix}quotesislami*
║┣❏ *${prefix}listsurah*
║┣❏ *${prefix}doaharian*
║┣❏ *${prefix}asmaulhusna*
║┣❏ *${prefix}niatsholat*
║┣❏ *${prefix}bacaansholat*
║┣❏ *${prefix}jadwalsholat*
║┣❏ *${prefix}kisahnabi*
║┣❏ *${prefix}tahlil*
║┣❏ *${prefix}ayatkursi*
║┣❏ *${prefix}hadits*
║┣❏ *${prefix}quran*
║┃
║┣━━⊱*「 𝗡𝗘𝗪𝗦 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏  *${prefix}cnnindonesia*
║┣❏  *${prefix}cnnnasional*
║┣❏  *${prefix}jadwaltv*
║┣❏  *${prefix}jadwaltvnow*
║┣❏  *${prefix}newsinfo*
║┣❏  *${prefix}cnninternasional*
║┣❏  *${prefix}infogempa*
║┣❏  *${prefix}liputan6*
║┣❏  *${prefix}cnnnews*
║┣❏  *${prefix}republika*
║┣❏  *${prefix}temponews*
║┣❏  *${prefix}kumparannews*
║┣❏  *${prefix}lazymedia*
║┣❏  *${prefix}resepmakanan*
║┃
║┣━━⊱*「 𝗠𝗢𝗩𝗜𝗘 𝗦𝗧𝗢𝗥𝗬 」* 
║┃
║┣❏ *${prefix}ik21*
║┣❏ *${prefix}wattpad*
║┣❏ *${prefix}cerpen*
║┣❏ *${prefix}ceritahoror*
║┣❏ *${prefix}drakorongoing*
║┣❏*${prefix}wattpadsearch*
║┃
║┣━━⊱*「 𝗠𝗘𝗗𝗜𝗔 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}beritahoax*
║┣❏ *${prefix}amv*
║┣❏ *${prefix}brainly*
║┣❏ *${prefix}pinterest*
║┣❏ *${prefix}randomhusbu*
║┣❏ *${prefix}randomcyberspace*
║┣❏ *${prefix}randomgame*
║┣❏ *${prefix}ytmp3*
║┣❏ *${prefix}ytmp4*
║┣❏ *${prefix}shopee*
║┣❏ *${prefix}play*
║┣❏ *${prefix}play2*
║┣❏ *${prefix}ytsearch*
║┣❏ *${prefix}google*
║┣❏ *${prefix}randommountain*
║┣❏ *${prefix}nangis*
║┣❏ *${prefix}bokep*
║┣❏ *${prefix}blowjob*
║┣❏ *${prefix}xnxx*
║┣❏ *${prefix}xnxxsearch*
║┣❏ *${prefix}xhamster*
║┣❏ *${prefix}xhamstersearch*
║┣❏ *${prefix}pixiv*
║┣❏ *${prefix}pixivdl*
║┣❏ *${prefix}youtubedl*
║┣❏ *${prefix}randomloli*
║┣❏ *${prefix}randomprogramer*
║┣❏ *${prefix}meme*
║┣❏ *${prefix}memeindo*
║┣❏ *${prefix}telesticker*
║┣❏ *${prefix}tiktoknowm*
║┣❏ *${prefix}tiktokmusic*
║┣❏ *${prefix}spotify*
║┣❏ *${prefix}spotifysearch*
║┣❏ *${prefix}jooxplay*
║┣❏ *${prefix}igdl*
║┣❏ *${prefix}fbdl*
║┣❏ *${prefix}zippyshare*
║┣❏ *${prefix}pinterest*
║┣❏ *${prefix}pinterestdl*
║┣❏ *${prefix}tts*
║┣❏ *${prefix}joox*
║┣❏ *${prefix}lirik*
║┣❏ *${prefix}ssweb*
║┣❏ *${prefix}map*
║┣❏ *${prefix}stalkig*
║┣❏ *${prefix}afk*
║┣❏ *${prefix}unafk*
║┃
║┣━━⊱*「 𝗦𝗢𝗨𝗡𝗗 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}sound*
║┣❏ *${prefix}sound1*
║┣❏ *${prefix}sound2*
║┣❏ *${prefix}sound3*
║┣❏ *${prefix}sound4*
║┣❏ *${prefix}sound5*
║┣❏ *${prefix}sound6*
║┣❏ *${prefix}sound7*
║┣❏ *${prefix}sound8*
║┣❏ *${prefix}sound9*
║┣❏ *${prefix}sound10*
║┣❏ *${prefix}sound11*
║┣❏ *${prefix}sound12*
║┣❏ *${prefix}sasageyo*
║┣❏ *${prefix}welot*
║┣❏ *${prefix}ganteng*
║┣❏ *${prefix}gatal*
║┣❏ *${prefix}alay*
║┣❏ *${prefix}pota*
║┣❏ *${prefix}texttovn*
║┃
║┣━━⊱*「 𝗟𝗜𝗠𝗜𝗧 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}limit*
║┣❏ *${prefix}buylimit*
║┣❏ *${prefix}dompet*
║┃
║┣━━⊱*「 𝗣𝗟𝗔𝗦𝗧𝗜𝗤 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}exo*
║┣❏ *${prefix}bts*
║┃
║┣━━⊱*「 𝗡𝗦𝗙𝗪 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}hentai*
║┣❏ *${prefix}pokemon*
║┣❏ *${prefix}anjing*
║┣❏ *${prefix}nsfwloli*
║┣❏ *${prefix}nsfwneko*
║┣❏ *${prefix}solo*
║┣❏ *${prefix}nsfwtrap*
║┣❏ *${prefix}nsfwpussy*
║┣❏ *${prefix}nsfwyuri*
║┣❏ *${prefix}ero*
║┣❏ *${prefix}nsfwloli2*
║┣❏ *${prefix}sideoppai*
║┣❏ *${prefix}nsfwwaifu*
║┣❏ *${prefix}ecchi*
║┣❏ *${prefix}nekopoi* <judul>
║┃
║┣━━⊱*「 𝗚𝗥𝗢𝗨𝗣 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}hidetag*
║┣❏ *${prefix}del*
║┣❏ *${prefix}grouplist*
║┣❏ *${prefix}level*
║┣❏ *${prefix}leaderboard*
║┣❏ *${prefix}linkgc*
║┣❏ *${prefix}tagall*
║┣❏ *${prefix}setpp*
║┣❏ *${prefix}add*
║┣❏ *${prefix}kick*
║┣❏ *${prefix}setname*
║┣❏ *${prefix}wame*
║┣❏ *${prefix}setdesc*
║┣❏ *${prefix}demote*
║┣❏ *${prefix}promote*
║┣❏ *${prefix}listadmin*
║┣❏ *${prefix}group* [buka/tutup]
║┣❏ *${prefix}leveling* [enable/disable]
║┣❏ *${prefix}nsfw* [1/0]
║┣❏ *${prefix}simih* [1/0]
║┣❏ *${prefix}antilinkgrup* [1/0]
║┣❏ *${prefix}welcome* [1/0]
║┃
║┣━━⊱*「 𝗢𝗪𝗡𝗘𝗥 𝗠𝗘𝗡𝗨 」* 
║┃
║┣❏ *${prefix}bc*
║┣❏ *${prefix}bcgc*
║┣❏ *${prefix}kickall*
║┣❏ *${prefix}setreply*
║┣❏ *${prefix}addlimit*
║┣❏ *${prefix}setlimit*
║┣❏ *${prefix}setnamabot*
║┣❏ *${prefix}setprefix*
║┣❏ *${prefix}setvhtear*
║┣❏ *${prefix}setonlydev*
║┣❏ *${prefix}setlolhuman*
║┣❏ *${prefix}antilinkgrup* [1/0]
║┣❏ *${prefix}antidelete* [1/0]
║┣❏ *${prefix}clearall*
║┣❏ *${prefix}ban*
║┣❏ *${prefix}unban*
║┣❏ *${prefix}block*
║┣❏ *${prefix}unblock*
║┣❏ *${prefix}setmemberlimit*
║┣❏ *${prefix}addbadword* <teks>
║┣❏ *${prefix}listbadword*
║┣❏ *${prefix}nobadword*
║┣❏ *${prefix}listblock*
║┣❏ *${prefix}leave*
║┣❏ *${prefix}event* [1/0]
║┣❏ *${prefix}clone*
║┣❏ *${prefix}setbotpp*
║┃
║┣━━⊱*「 Thanks To 」* 
║┃
║┣❏ RIKKA
║┃
║┗━━━━*《 ${namabot} 》*
╚═════════════════❍
` 
