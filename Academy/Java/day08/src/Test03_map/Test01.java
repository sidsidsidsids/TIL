package Test03_map;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Test01 {
	public static void main(String[] args) {
		Map<String, String> map = new HashMap<>();
		
		// 맵에 값 저장  
		map.put("Hong", "010-1111-2222");
		map.put("ong", "010-1311-2222");
		map.put("Hon", "010-4411-2222");
		map.put("ong", "010-1311-2222");
		
		// 중복값은 새 값으로 대체됨  
		System.out.println(map);
		
		System.out.println(map.get("Hon"));
		System.out.println(map.get("Kim"));
		
		System.out.println(map.containsKey("Kim"));
		
		System.out.println(map.containsValue("010-1111-2222"));
		
		for(Map.Entry<String, String> entry: map.entrySet()) {
			System.out.println(entry.getKey()+" : "+entry.getValue());
		}
		
		Iterator<String> e = map.keySet().iterator();
		while(e.hasNext()) {
			String Key = e.next();
			System.out.printf("키: %s, 값: %s \n", Key, map.get(Key));
		}
		
		for(String Key : map.keySet()) {
			System.out.printf("키: %s, 값: %s \n", Key, map.get(Key));
		}
		
		System.out.println(map.size());
	}
}
