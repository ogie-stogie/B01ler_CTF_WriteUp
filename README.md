# B01ler_CTF_WriteUp
[Write Up Link](https://github.com/tbart27/B01ler_CTF_WriteUp/blob/master/README.md)

### Team: 466 Crew
Taylor Bart<br>
John Tiffany<br>
James Kabat<br>
Bryan Ibarra<br>
<br>
### Crypto: Dream Stealing
For this challenge I figured out that the file contained values used for an RSA encryption. More specifically, I was able to see that I was given the n, p and e values along with the cypher message. By using RsaCtfTool, I was able to return the flag with the command:<br>
<br>
./RsaCtfTool.py -n 98570307780590287344989641660271563150943084591122129236101184963953890610515286342182643236514124325672053304374355281945455993001454145469449640602102808287018619896494144221889411960418829067000944408910977857246549239617540588105788633268030690222998939690024329717050066864773464183557939988832150357227 -p 9695477612097814143634685975895486365012211256067236988184151482923787800058653259439240377630508988251817608592320391742708529901158658812320088090921919 -e 65537 --uncipher 75665489286663825011389014693118717144564492910496517817351278852753259053052732535663285501814281678158913989615919776491777945945627147232073116295758400365665526264438202825171012874266519752207522580833300789271016065464767771248100896706714555420620455039240658817899104768781122292162714745754316687483<br>
And here is the result I obtained: flag{4cce551ng_th3_subc0nsc10us}<br>
### Crypto: Totem
In this challenge, we were given a python template code for submitting data to a server. When first accessing the site, you would see that you were asked to decrypt various encryptions correctly. If one was wrong then you would have to start over. John then joined me on this challenege and we looked into the totem.py file that was given. We could see we were given the template for automating 1000 decryptions with four methods (atbash, baconian, base64, rot13). With these two files (totem.py and decrypt_bacon), we were able to get this output (with test print statements):<br><br>
[terminal picture]<br><br>
After 1000 iterations we received this flag: ctf{4n_313g4nt_s01ut10n_f0r_tr4cking_r341ity}
### Crypto World: G1 (Mini-Challenge)

### PWN: There is no Spoon

### Conclusion
We were able to find 4 flags as a team (albeit one was a mini flag).
