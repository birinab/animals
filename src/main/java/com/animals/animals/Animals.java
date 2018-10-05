package com.animals.animals;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.*;

@Document
public class Animals {

    @Id
    private String id;

    private String name;
    private String Kingdom;
    private String Phylum;
    private String Klass;
    private String Order;
    private String Family;
    private String Genus;
    private String ScientificName;
    private String Type;
    private String Diet;
    private String Size;
    private String Weight;
    private String TopSpeed;
    private String Lifespan;
    private String Lifestyle;
    private String Do;
    private String Dont;

    public Animals() {}

    public String getName() {
        return name;
    }

    public void setName(String name) {
        name = name;
    }

    public String getKingdom() {
        return Kingdom;
    }

    public void setKingdom(String kingdom) {
        Kingdom = kingdom;
    }

    public String getPhylum() {
        return Phylum;
    }

    public void setPhylum(String phylum) {
        Phylum = phylum;
    }

    public String getKlass() {
        return Klass;
    }

    public void setKlass(String Klass) {
        Klass = Klass;
    }

    public String getOrder() {
        return Order;
    }

    public void setOrder(String order) {
        Order = order;
    }

    public String getFamily() {
        return Family;
    }

    public void setFamily(String family) {
        Family = family;
    }

    public String getGenus() {
        return Genus;
    }

    public void setGenus(String genus) {
        Genus = genus;
    }

    public String getScientificName() {
        return ScientificName;
    }

    public void setScientificName(String scientificName) {
        ScientificName = scientificName;
    }

    public String getType() {
        return Type;
    }

    public void setType(String type) {
        Type = type;
    }

    public String getDiet() {
        return Diet;
    }

    public void setDiet(String diet) {
        Diet = diet;
    }

    public String getSize() {
        return Size;
    }

    public void setSize(String size) {
        Size = size;
    }

    public String getWeight() {
        return Weight;
    }

    public void setWeight(String weight) {
        Weight = weight;
    }

    public String getTopSpeed() {
        return TopSpeed;
    }

    public void setTopSpeed(String topSpeed) {
        TopSpeed = topSpeed;
    }

    public String getLifespan() {
        return Lifespan;
    }

    public void setLifespan(String lifespan) {
        Lifespan = lifespan;
    }

    public String getLifestyle() {
        return Lifestyle;
    }

    public void setLifestyle(String lifestyle) {
        Lifestyle = lifestyle;
    }

    public String getDo() {
        return Do;
    }

    public void setDo(String aDo) {
        Do = aDo;
    }

    public String getDont() {
        return Dont;
    }

    public void setDont(String dont) {
        Dont = dont;
    }
}
