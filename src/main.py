rdf_data = """<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.semanticweb.org/mael2/ontologies/2023/4/transport/"
     xml:base="http://www.semanticweb.org/mael2/ontologies/2023/4/transport/"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:transport="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#">
    <owl:Ontology rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport"/>
    

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#connects">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#employs">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#hasDestination">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#hasInfrastructure">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:ObjectProperty>
    
    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#hasOrigine">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#hasPeople">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#hasTransportMode">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#offersService">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:ObjectProperty>
 
    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#preferredBy">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:ObjectProperty>
    
    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#providesJourney">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#serves">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#usesEnergy">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Energy"/>
    </owl:ObjectProperty>
    
    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#capacity">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#carbonEmission">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
    </owl:DatatypeProperty>
    
    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#cost">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#distance">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#duration">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#endDate">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#dateTime"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#speed">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#startDate">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#dateTime"/>
    </owl:DatatypeProperty>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AirlineCompany">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Boat">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BoatCompany">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Bus">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusCompany">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Car">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:Class>
    
    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CarCompany">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CheapJourney">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#cost"/>
                        <owl:someValuesFrom>
                            <rdfs:Datatype>
                                <owl:onDatatype rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
                                <owl:withRestrictions rdf:parseType="Collection">
                                    <rdf:Description>
                                        <xsd:maxInclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">50</xsd:maxInclusive>
                                    </rdf:Description>
                                </owl:withRestrictions>
                            </rdfs:Datatype>
                        </owl:someValuesFrom>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Destination"/>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricBus">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Bus"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricCar">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Car"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Energy"/>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ExpensiveJourney">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#cost"/>
                        <owl:someValuesFrom>
                            <rdfs:Datatype>
                                <owl:onDatatype rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
                                <owl:withRestrictions rdf:parseType="Collection">
                                    <rdf:Description>
                                        <xsd:minInclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">200</xsd:minInclusive>
                                    </rdf:Description>
                                </owl:withRestrictions>
                            </rdfs:Datatype>
                        </owl:someValuesFrom>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fossil">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Energy"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridBus">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Bus"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridCar">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Car"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>


    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#LongJourney">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#duration"/>
                        <owl:someValuesFrom>
                            <rdfs:Datatype>
                                <owl:onDatatype rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
                                <owl:withRestrictions rdf:parseType="Collection">
                                    <rdf:Description>
                                        <xsd:minInclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">6</xsd:minInclusive>
                                    </rdf:Description>
                                </owl:withRestrictions>
                            </rdfs:Datatype>
                        </owl:someValuesFrom>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
    </owl:Class>
    
    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Motorboat">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Boat"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Passengers">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Pilot">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#People"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Plane">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Energy"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sailboat">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Boat"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ShortJourney">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#duration"/>
                        <owl:someValuesFrom>
                            <rdfs:Datatype>
                                <owl:onDatatype rdf:resource="http://www.w3.org/2001/XMLSchema#decimal"/>
                                <owl:withRestrictions rdf:parseType="Collection">
                                    <rdf:Description>
                                        <xsd:maxInclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2</xsd:maxInclusive>
                                    </rdf:Description>
                                </owl:withRestrictions>
                            </rdfs:Datatype>
                        </owl:someValuesFrom>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalBus">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Bus"/>
    </owl:Class>
    
    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalCar">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Car"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Train">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainCompany">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Company"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Infrastructure"/>
    </owl:Class>

    <owl:Class rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TransportMode"/>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AirFrance">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AirlineCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Elouan"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airbus_A320">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Plane"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Kérosène"/>
    </owl:NamedIndividual>
    
    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Alexander_Dennis_Enviro400H">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Alexandre">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Allemagne">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Alès">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Antoine">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Axel">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Azimut_Atlantis_45">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Motorboat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Barcelone"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BYD_K9">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Rome">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <transport:hasDestination rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome"/>
        <transport:hasOrigine rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin"/>
        <transport:hasPeople rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Alexandre"/>
        <transport:hasTransportMode rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Solaris_Urbino"/>
        <transport:carbonEmission rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">44</transport:carbonEmission>
        <transport:cost rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">210</transport:cost>
        <transport:distance rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">1500</transport:distance>
        <transport:duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">26</transport:duration>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Biocarburant">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Boeing_737">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Plane"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Kérosène"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Corsair">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AirlineCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fanny"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CostaCruises">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BoatCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Manon"/>
    </owl:NamedIndividual>


    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CroisiEurope">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BoatCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Louis"/>
    </owl:NamedIndividual>
    

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Deutsche_Bahn">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Maxime"/>
    </owl:NamedIndividual>
    
    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fossil"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Elouan">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Pilot"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Emma">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Espagne">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fossil"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#EuropCar">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CarCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Emma"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fanny">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Pilot"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#FlixBus">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Alexandre"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#France">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_Alès">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_centrale_de_Berlin">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Barcelone-Sants">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_centrale_de_Berlin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Roma_Termini"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Barcelone-Sants"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Nîmes"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Nîmes">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Roma_Termini"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_centrale_de_Berlin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Barcelone-Sants"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Roma_Termini">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Nîmes"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gaëtan">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Passengers"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Genêve">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Hamza">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Passengers"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Honda_Accord_Hybrid">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Hydrogène">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Italie">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Jeanneau_Sun_Odyssey_440">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sailboat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Barcelone"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Éolienne"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Kérosène">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Fossil"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Lagoon_450S">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sailboat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Civitavecchia"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Éolienne"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Lexus_RX_Hybrid">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Louis">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Léa">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Manon">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Mathieu">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Maxime">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Maël">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Passengers"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Mercedes-Benz_C-Class">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Mercedes-Benz_Citaro">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nicolas">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Pilot"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nissan_Leaf">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#OUIGO">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Train"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_Alès"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Nîmes"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#OuiBus">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Léa"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Berlin-Brandebourg"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Nîmes">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Journey"/>
        <transport:hasDestination rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes"/>
        <transport:hasOrigine rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris"/>
        <transport:hasPeople rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sarah"/>
        <transport:hasTransportMode rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#OUIGO"/>
        <transport:carbonEmission rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">4.1</transport:carbonEmission>
        <transport:cost rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">32.5</transport:cost>
        <transport:distance rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">690</transport:distance>
        <transport:duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">3</transport:duration>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Peugeot_308">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Barcelone">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Civitavecchia"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Civitavecchia">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Barcelone"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rent-A-Car">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#CarCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Mathieu"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rogério">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Passengers"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#City"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BusStation"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
    </owl:NamedIndividual>
    
    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Rome_Fiumicino">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Airport"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Aéroport_international_de_Genève"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Barcelone-El_Prat"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Montpellier-Méditerranée"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nîmes-Alès-Camargue-Cévennes"/>
        <transport:connects rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Paris-Charles-de-Gaulle"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RyanAir">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AirlineCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Nicolas"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#SNCF">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sarah"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sarah">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Sea_Ray_Sundancer_350">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Motorboat"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Port_de_Civitavecchia"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Solaire">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Solaris_Urbino">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ThermalBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#GenêveGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#NîmesGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Diesel"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Suisse">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Country"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TER">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Train"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_centrale_de_Berlin"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Barcelone-Sants"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TGV">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Train"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_centrale_de_Berlin"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Barcelone-Sants"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Genève-Cornavin"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Montpellier-Saint-Roch"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Paris-Saint-Lazare"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Gare_de_Roma_Termini"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Tesla_Model_S">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricCar"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BerlinGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#MontpellierGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Thomas">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Driver"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrenItalia">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#TrainCompany"/>
        <transport:employs rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Thomas"/>
    </owl:NamedIndividual>
    
    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Volvo_7900_Electric">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ElectricBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#BarceloneNordGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#RomeGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Volvo_7900_Hybrid">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#HybridBus"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#AlèsGareRoutière"/>
        <transport:hasInfrastructure rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#ParisGareRoutière"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Essence"/>
        <transport:usesEnergy rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Électricité">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable"/>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Éolienne">
        <rdf:type rdf:resource="http://www.semanticweb.org/mael2/ontologies/2023/4/transport#Renewable"/>
    </owl:NamedIndividual>
</rdf:RDF>

"""

from rdflib import Graph
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from style import apply_style

# Charger l'image du logo
def load_logo(window):
    # image = Image.open('/assets/bus.jpg')  # Remplacez 'car_logo.png' par le nom du fichier ou l'URL de votre image
    image = Image.open('bus.jpg')  # Remplacez 'car_logo.png' par le nom du fichier ou l'URL de votre image

    # Réduire la taille de l'image si nécessaire
    image = image.resize((100, 100), Image.ANTIALIAS)

    # Convertir l'image en image Tkinter
    logo = ImageTk.PhotoImage(image)

    # Créer un label pour l'image
    logo_label = tk.Label(window, image=logo)
    logo_label.image = logo  # Conserver une référence à l'image
    logo_label.pack(pady=10)  # Afficher l'image

# Fonction pour exécuter une requête SPARQL et retourner les résultats sous forme de liste
def execute_sparql_query(g, query):
    results = g.query(query)
    return list(results)

def display_category():
    query = """
    SELECT DISTINCT ?category ?individual WHERE {
        ?individual a ?category .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Toutes les catégories")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("individual", "category")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("individual", anchor=tk.W, width=200)
    table.column("category", anchor=tk.W, width=150)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("individual", text="Individual", anchor=tk.W)
    table.heading("category", text="Category", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        individual = str(result.individual).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        category = str(result.category).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        table.insert("", tk.END, text=str(i+1), values=(individual, category))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_transport_prices():
    query = """
    SELECT ?journey ?transportMode ?price ?duration ?distance ?carbonEmission WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      ?journey transport:duration ?duration .
      ?journey transport:distance ?distance .
      ?journey transport:carbonEmission ?carbonEmission .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Prix Transports")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price", "duration", "distance", "carbonEmission")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=150)
    table.column("price", anchor=tk.W, width=100)
    table.column("duration", anchor=tk.W, width=100)
    table.column("distance", anchor=tk.W, width=100)
    table.column("carbonEmission", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)
    table.heading("duration", text="Duration", anchor=tk.W)
    table.heading("distance", text="Distance", anchor=tk.W)
    table.heading("carbonEmission", text="Carbon Emission", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        duration = str(result.duration)
        distance = str(result.distance)
        carbon_emission = str(result.carbonEmission)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price, duration, distance, carbon_emission))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)
    
def display_cheapest_transport_prices():
    # Requête SPARQL pour récupérer les trajets avec les prix les moins chers
    query = """
    SELECT ?journey ?transportMode ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      FILTER NOT EXISTS {
        ?journey transport:cost ?cheaperPrice .
        ?cheaperJourney rdf:type transport:Journey .
        ?cheaperJourney transport:hasTransportMode ?transportMode .
        ?cheaperJourney transport:cost ?cheaperPrice .
        FILTER (?cheaperPrice < ?price)
      }
    }
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Le transport le moins cher")
    window.geometry("600x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=200)
    table.column("price", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_least_polluting_transport():
    # Requête SPARQL pour récupérer le moyen de transport le moins polluant avec son prix
    query = """
    SELECT ?transportMode ?carbonEmission ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:carbonEmission ?carbonEmission .
      ?journey transport:cost ?price .
    }
    GROUP BY ?transportMode ?carbonEmission ?price
    ORDER BY ASC(?carbonEmission)
    LIMIT 1
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Récupération du résultat
    if results:
        transport_mode = str(results[0].transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        carbon_emission = str(results[0].carbonEmission)
        price = str(results[0].price)
        message = f"Le transport le moins polluant est le(a) {transport_mode} avec une emission carbonne de {carbon_emission} et un prix de {price}. Valider."

        # Affichage du message dans une boîte de dialogue
        messagebox.showinfo("Transport moins polluant", message)
    else:
        # Affichage d'un message d'erreur si aucun résultat n'est trouvé
        messagebox.showerror("Error", "No data found.")


# Chargement des données RDF
g = Graph()
g.parse(data =rdf_data, format='xml')
# g.parse(r"/data/transport.rdf", format="xml")

# Création de la fenêtre principale
window = tk.Tk()
window.title("EcoTrip")
window.geometry("400x300")
window.configure(background='white')

# Charger le logo
load_logo(window)

# Création du conteneur principal
container = ttk.Frame(window)
container.pack(fill=tk.BOTH, expand=True)

# Appliquer le style
apply_style()

# Création des boutons pour afficher les tables
transport_prices_button = ttk.Button(container, text="Prix transports", command=display_transport_prices)
transport_prices_button.pack(pady=10)

least_polluting_transport_button = ttk.Button(container, text="Moins polluant", command=display_least_polluting_transport)
least_polluting_transport_button.pack(pady=10)

transport_categories_button = ttk.Button(container, text="Categories", command=display_category)
transport_categories_button.pack(pady=10)

# Boucle principale de l'interface graphique
window.mainloop()
