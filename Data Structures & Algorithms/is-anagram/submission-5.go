func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	seens := make(map[byte]int)
	seent := make(map[byte]int)

	for i := range(s) {
		sv := s[i]
		tv := t[i]

		seens[sv] +=1
		seent[tv] +=1
	}

	for ks, vs := range seens {
		if vt, ok := seent[ks]; !ok || vt != vs  {
			return false
		}
	}

	for kt, vt := range seent {
		if vs, ok := seens[kt]; !ok || vt != vs {
			return false
		}
	}

	return true
}
