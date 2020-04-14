import java.util.ArrayList;
import java.util.Scanner;

class DynamicArray{
    private ArrayList<Object> liste;
    private int size,inObj; //boyutu ve eleman sayıları tutuluyor

    //yapıcı metodlar burada bulunuyor
    public DynamicArray(){
        size = 0;
        inObj = 0;
    }
    public DynamicArray(Object [] liste){
        this.liste = new ArrayList<Object>(liste.length);
        for(int i = 0; i< liste.length; i++){
            this.liste.add(liste[i]);
        }
        size = liste.length; //boyut set ediliyor
        inObj = size; //boyut kadar eleman olduğu için o kadar eleman olduğu set ediliyor
    }

    public Object remove(){ //pop fonksiyonu 
        if(inObj != 0){ //içinde eleman olup olmadığını kontrol ediyor
            int l = liste.size();
            ArrayList<Object> nList = new ArrayList<Object>(liste.size());
            for(int i=0; i<l-1; i++){ //liste yeniden yapılıyor
                nList.add(liste.get(i));
            }
            Object r = liste.get(l-1);
            liste = nList;
            inObj--; //eleman sayısı bir azaltılıyor
            return r;
        }else{
            return null; //içinde eleman yoksa 
        }
    }

    public void append(Object tempObject) {
        if(inObj == size){ // eleman sayısı boyuta eşit ise
            resizeOneObject(); //boyut artırılır
            liste.add(tempObject); //eleman eklenir
            inObj++; //eleman sayısı bir artırılır
        }else{
            liste.add(tempObject); //eğer eleman sayısı sınırda değilse eleman eklenir
            inObj++; //eleman sayısı artırılır
        }
    }

    //liste resize edildi fakat sadece 1 eleman eklenebilir hale getirildi
    private void resizeOneObject(){
        ArrayList<Object> mArrayList = new ArrayList<Object>();
        for(int i = 0; i < liste.size(); i++){ //yeni büyük boyutlu liste oluşturuluyor 
            mArrayList.add(liste.get(i));
        }
        liste = mArrayList;
        size++; //boyut artırılıyor
    }
}

